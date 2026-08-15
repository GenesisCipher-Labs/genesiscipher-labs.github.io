#!/usr/bin/env ruby
# frozen_string_literal: true
#
# build-faq-data.rb — regenerate _data/faq.yml from pact-faq.md
#
# WHY THIS EXISTS
# Google requires that an answer declared in FAQPage markup be VISIBLE on the
# page carrying it, and an extractor that finds markup disagreeing with the body
# text has reason to distrust the whole page. Hand-copying the answers into a
# data file satisfies that on the day it is written and breaks silently the next
# time the page is edited — the same "second copy that drifts" failure this
# project refuses everywhere else.
#
# So the data file is DERIVED, not authored. Edit pact-faq.md, run this, commit
# both. There is one copy of each answer and it is the one readers see.
#
#   ruby tools/build-faq-data.rb
#
# Run it from the site repo root (or from AppStore/web/ in the Pact repo — the
# paths below are relative to the working directory).
#
# It reads every "### question" under every "## section" heading in pact-faq.md,
# takes the paragraphs beneath it as the answer, strips Markdown emphasis, links
# and code ticks so the JSON carries plain prose, and writes _data/faq.yml.
# It is idempotent and it fails loudly rather than writing a partial file.

require "yaml"

SOURCE = ENV.fetch("FAQ_SOURCE", "pact-faq.md")
TARGET = ENV.fetch("FAQ_TARGET", "_data/faq.yml")
# The URL of the page the answers are visible on. The FAQPage markup is emitted
# only on this page; if the FAQ ever moves, change it here and in
# _includes/head-custom.html together.
PAGE_URL = "/pact/faq/"

abort "cannot read #{SOURCE} (run me from the site repo root)" unless File.readable?(SOURCE)

body = File.read(SOURCE)
# Drop YAML front matter so a "---" inside it is never mistaken for a rule.
body = body.sub(/\A---\s*\n.*?\n---\s*\n/m, "")

def demarkdown(text)
  text
    .gsub(/\[([^\]]+)\]\([^)]*\)/, '\1') # [label](url) -> label
    .gsub(/\*\*([^*]+)\*\*/, '\1')       # **bold**     -> bold
    .gsub(/(?<!\*)\*([^*\n]+)\*(?!\*)/, '\1') # *italic* -> italic
    .gsub(/`([^`]+)`/, '\1')             # `code`       -> code
    .gsub(/\s+/, " ")
    .strip
end

entries = []
section = nil
question = nil
buffer = []

flush = lambda do
  next if question.nil?
  answer = demarkdown(buffer.join("\n"))
  if answer.empty?
    abort "question with no answer text: #{question.inspect}"
  end
  entries << { "section" => section, "q" => demarkdown(question), "a" => answer }
  question = nil
  buffer = []
end

body.each_line do |line|
  case line
  when /\A##\s+(?!#)(.+)/ then flush.call; section = demarkdown(Regexp.last_match(1))
  when /\A###\s+(.+)/     then flush.call; question = Regexp.last_match(1)
  when /\A#\s+/           then flush.call
  when /\A-{3,}\s*\z/     then flush.call
  else buffer << line if question
  end
end
flush.call

abort "no questions found in #{SOURCE} — has its heading level changed?" if entries.empty?

# group_by rather than tally, so this runs on the system Ruby (2.6) as well as
# on whatever the founder's rbenv is pointing at.
dupes = entries.map { |e| e["q"] }.group_by(&:itself).select { |_, v| v.length > 1 }.keys
abort "duplicate questions, which would produce duplicate FAQPage entries: #{dupes.inspect}" if dupes.any?

short = entries.select { |e| e["a"].length < 40 }
abort "suspiciously short answers (markdown parsed wrongly?): #{short.map { |e| e['q'] }.inspect}" if short.any?

header = <<~YAML
  # GENERATED FILE — DO NOT EDIT BY HAND.
  #
  # Regenerate with:  ruby tools/build-faq-data.rb
  #
  # Source of truth: #{SOURCE} (published at #{PAGE_URL}).
  # Every answer below is the visible text of that page with Markdown stripped,
  # which is what Google requires of FAQPage markup and what makes the JSON-LD
  # trustworthy to an extractor. Edit the page, re-run the script, commit both.
  #
  # Consumed by: _includes/head-custom.html (FAQPage JSON-LD) and llms.txt.
  # Questions: #{entries.length}
YAML

File.write(TARGET, header + { "page_url" => PAGE_URL, "questions" => entries }.to_yaml.sub(/\A---\n/, "\n"))

puts "wrote #{TARGET}: #{entries.length} questions across #{entries.map { |e| e['section'] }.uniq.length} sections"
entries.each { |e| puts "  [#{e['section']}] #{e['q']}" }
