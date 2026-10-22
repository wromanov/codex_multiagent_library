---
name: activity-progress-reporting
description: Add truthful periodic execution progress telemetry to nontrivial Codex work while preserving the agent's normal user-visible updates.
---

# Activity Progress Reporting v1.1

Use this skill for nontrivial work that spans multiple meaningful steps, such as investigation, research, implementation, or a tool-driven workflow. Skip it for a one-step answer or tiny edit unless the user asks for progress reporting.

## Core rule: additive telemetry

This skill adds progress telemetry to the agent's communication. It must never replace, suppress, reformat, or delay the agent's normal user-visible execution updates. Preserve useful updates about findings, decisions, implementation, validation, and blockers.

Do not turn every update into a telemetry-only message. When a normal update is naturally due near a checkpoint, keep its content and append the telemetry block. When no normal update is due, send a concise telemetry-only update to report the checkpoint. Do not claim to reveal private reasoning; report observable work, decisions, and status.

## Reporting cadence

At the beginning of nontrivial work, identify the activity and the main completion milestones. Estimate completion from those milestones, based on completed work rather than tool-call count or elapsed time.

For sustained work, report progress at each 4 percentage-point checkpoint reached: 4%, 8%, 12%, and so on through 96%, then report 100% when the activity is complete. Keep percentages monotonic and use multiples of 4. Estimates are approximate; do not imply more precision than the work supports.

Do not fabricate intermediate progress for a short or atomic task. If the task finishes before a checkpoint is meaningfully reached, report the result at 100%. If one genuinely atomic step crosses several checkpoints, report the current honest checkpoint once instead of backfilling a burst of updates.

If work is blocked or ends incomplete, report the honest current percentage with BLOCKED or PARTIAL; do not label incomplete work COMPLETED or report 100%.

## Telemetry format

Append this compact block to the normal update when possible:

[EXECUTION TELEMETRY]
ACTIVITY: <short name for the requested activity>
ACTIVITY_COMPLETION_PERCENT: <multiple of 4 from 4% to 100%>
CURRENT_STEP: <current milestone>
STATUS: IN_PROGRESS | BLOCKED | PARTIAL | COMPLETED

Use the user's language for the activity and step descriptions. At completion, use 100% and COMPLETED only when the requested outcome is actually complete. Include a concise RESULT: line in the final telemetry block.
