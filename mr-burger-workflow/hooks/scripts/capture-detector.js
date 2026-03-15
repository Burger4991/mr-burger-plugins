#!/usr/bin/env node

/**
 * Capture Detector Hook
 *
 * Runs on UserPromptSubmit and detects brain-dump patterns.
 * If detected, suggests using the /capture command.
 *
 * Patterns detected:
 * - "remind me to...", "i need to...", "don't forget...", "add to my tasks...", "note to self..."
 * - Loose comma-separated lists of things to do
 * - "I was thinking about..." type musings
 * - "brain dump", "brain dump", "dump", etc.
 *
 * Input: JSON from stdin with "prompt" field
 * Output: Router message if detected, silent if not
 * Exit code: Always 0 (success)
 */

const readline = require('readline');

// Brain dump detection patterns
const brainDumpPatterns = [
  /remind\s+me\s+to/i,
  /i\s+need\s+to/i,
  /don't\s+forget/i,
  /add\s+to\s+my\s+tasks/i,
  /note\s+to\s+self/i,
  /i\s+was\s+thinking/i,
  /brain\s+dump/i,
  /just\s+dump/i,
  /random\s+thoughts/i,
  /loose\s+thoughts/i,
  /rambl/i,  // ramble, rambling, ramblings
];

// Comma-separated list pattern (3+ comma-separated items suggests a list)
const listPattern = /^[^,\n]*,[^,\n]*,[^,\n]*/;

// Read input from stdin
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let inputData = '';

rl.on('line', (line) => {
  inputData += line;
});

rl.on('close', () => {
  try {
    // Parse JSON input
    const input = JSON.parse(inputData);
    const prompt = input.prompt || '';

    // Check for brain-dump patterns
    let isBrainDump = false;

    // Check explicit patterns
    for (const pattern of brainDumpPatterns) {
      if (pattern.test(prompt)) {
        isBrainDump = true;
        break;
      }
    }

    // Check for comma-separated lists (if not already detected)
    if (!isBrainDump && listPattern.test(prompt) && prompt.length > 50) {
      // Heuristic: if it's a moderate length with 3+ comma-separated items, might be a list
      isBrainDump = true;
    }

    // Output router message if brain dump detected
    if (isBrainDump) {
      console.log('--- Capture Detector ---');
      console.log('This looks like something to capture. Use /capture to route it to your Second Brain (INBOX, TASKS, or notes).');
      console.log('--- End Capture ---');
    }

    // Always exit with 0 (success)
    process.exit(0);
  } catch (error) {
    // If JSON parsing fails or any error occurs, exit silently with 0
    process.exit(0);
  }
});
