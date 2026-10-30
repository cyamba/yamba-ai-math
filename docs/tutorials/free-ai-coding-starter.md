# Free AI coding starter

## Choose a free route

Start with the browser lesson if you have never used a coding assistant. Then try the same project with an agent that can edit files on your computer. Allow about 15 minutes for each lesson.

| Route | What you get | Cost boundary |
| --- | --- | --- |
| Claude Free in a browser | Explanations, coding help and Artifacts | Free usage limits; Claude Code is excluded |
| OpenCode 2 with an explicitly free hosted model | An open-source agent that reads and edits your project | The app is MIT licensed; hosted free offers can change |
| Claude Code | Anthropic's coding agent | Requires eligible paid access or separately billed provider access |

Claude's [current plan comparison](https://claude.com/pricing) marks Claude Code unavailable on Free. OpenCode's [model pricing](https://opencode.ai/v2/docs/console/models/#pricing) lists free options, including Big Pickle at the date checked, 30 October 2026. Open-source software does not make every connected model free or open source. Start without a paid provider, billing details or auto-recharge.

## Try Claude in the browser

Open [Claude](https://claude.ai/) and create or sign in to a free account. Paste this:

> I am a complete beginner. Help me make a Celsius to Fahrenheit converter as a single HTML Artifact. It needs a labelled number input, a Convert button and a clear result. Use no external libraries or network calls. Explain the formula in plain language. Give me one step at a time and wait while I try it.

Try these three cases in the preview:

| Celsius | Expected Fahrenheit |
| --- | --- |
| 0 | 32 |
| 100 | 212 |
| -40 | -40 |

Then ask:

> Show me the line that calculates the answer. Explain each part. What should happen when the input is empty?

An Artifact is a small interactive preview inside the chat. It does not give Claude access to your local folders. If you reach the free limit, wait for the reset shown by Claude; payment is not needed to finish this introductory lesson.

## Install OpenCode

These instructions target Windows. For macOS or Linux, use the platform-specific download on the same official page.

1. Open the [OpenCode 2 installation page](https://opencode.ai/v2/docs/). Under the CLI downloads, choose Windows x64 for a typical Intel or AMD computer, or ARM64 for an ARM computer.
2. Extract the downloaded ZIP. Keep the extracted files together and find `opencode.exe`.
3. Open PowerShell from the Windows Start menu. Create a separate practice folder:

```powershell
$practiceFolder = Join-Path $env:USERPROFILE 'Documents\ai-first-project'
New-Item -ItemType Directory -Force -Path $practiceFolder
Set-Location -LiteralPath $practiceFolder
```

4. In Explorer, use **Copy as path** on the extracted executable. Back in PowerShell, run:

```powershell
$openCodeExe = (Read-Host 'Paste the full path to opencode.exe').Trim('"')
& $openCodeExe --standalone
```

This starts OpenCode in the practice folder. No Node.js installation is needed for our HTML exercise. The V2 documentation says Windows package managers are unsupported, so these instructions use the standalone download rather than an older npm command.

In OpenCode, enter `/models` and select a model explicitly labelled free. If none is offered, return to the Claude browser lesson; do not add billing just to continue. The [provider guide](https://opencode.ai/v2/docs/cli/providers/) explains `/connect` if an account connection is required. Do not paste an API key into a chat.

## First coding exercise

An agent can change real files. Keep this lesson inside the new practice folder and use sample data.

First ask for a plan:

> I am learning. We are in a new practice folder. Do not edit files yet. Propose a tiny single-file Celsius to Fahrenheit converter in index.html, with no dependencies or network requests. Explain what you would create and how I can test it.

Read the answer. Then ask:

> Create only index.html. Use a labelled number input, a Convert button, an accessible result area and an error for empty or invalid input. Keep the code short and explain the important lines. Ask before running commands or accessing anything outside this folder.

Read any requested file or command action before approving it. When the file is ready, open a second PowerShell window in the practice folder and run:

```powershell
Start-Process .\index.html
```

A browser should open the local file. Check 0, 100 and -40 against the table, then try an empty input. Ask the agent to explain a failure before fixing it.

The calculation is:

```javascript
const fahrenheit = celsius * 9 / 5 + 32;
```

To learn how a change works, ask:

> Add a Reset button. Before editing, explain which part of the file will change. Keep the converter's existing behaviour.

Success means you can explain the formula, demonstrate the three correct results, and describe the Reset change in your own words.

## Review and undo

Before a change you want to keep safe, make a simple backup in the practice folder:

```powershell
Copy-Item -LiteralPath .\index.html -Destination .\index.before.html
```

After the edit, compare the two files in your editor. Ask the assistant:

> Show the changes and explain why each one is needed. Did you change anything I did not request?

The OpenCode terminal supports `/undo` to revert the latest user message and the work following it, and `/redo` to restore that work. Check the file afterwards; the [TUI guide](https://opencode.ai/v2/docs/cli/tui/#history) describes this behaviour.

If you prefer the manual backup, restore it only inside this practice folder:

```powershell
Copy-Item -LiteralPath .\index.before.html -Destination .\index.html
```

Reopen the browser file and test again. This plan, small edit, review and test cycle is the main habit to carry into Claude Code later.

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| PowerShell cannot find the executable | Copy its full extracted path again, including the filename |
| A payment or paid-key screen appears | Stop that route and use Claude Free, or choose an available explicitly free model |
| A hosted free model is unavailable | Try another currently free entry; free offers are temporary |
| The browser shows no change | Save the file and reload the local page |
| A result is wrong | Report the input, expected result and actual result to the assistant |

Use public toy code for this first lesson. Hosting and data policies vary between providers. OpenCode's open-source licence covers the program, while a hosted model's terms govern its service.

The example prompts and reference arithmetic were checked when preparing this lesson. A fresh account's quota, installation and hosted-model session still need to be verified on the learner's computer. The old Gemini CLI free-quota pages conflict with its current repository transition notice, so they are not the installation route used here.

## Sources

Checked on 30 October 2026.

- [Claude plans and the Free versus Claude Code distinction](https://claude.com/pricing)
- [Claude Code overview and account requirements](https://code.claude.com/docs/en/overview)
- [OpenCode source and MIT licence](https://github.com/anomalyco/opencode)
- [OpenCode 2 platform downloads](https://opencode.ai/v2/docs/)
- [OpenCode model pricing and temporary free offers](https://opencode.ai/v2/docs/console/models/#free-models)
- [Model selection](https://opencode.ai/v2/docs/models/)
- [Provider connection](https://opencode.ai/v2/docs/cli/providers/)
- [Terminal review and undo commands](https://opencode.ai/v2/docs/cli/tui/)
- [Gemini CLI's current individual-access transition notice](https://github.com/google-gemini/gemini-cli)

This lesson introduces the workflow. It does not require a Claude Code subscription.
