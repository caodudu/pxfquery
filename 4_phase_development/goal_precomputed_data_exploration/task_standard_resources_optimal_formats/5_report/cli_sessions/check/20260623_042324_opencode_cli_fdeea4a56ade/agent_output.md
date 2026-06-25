This is a CyHex Checking stage prompt. Let me read the current state of all required files and perform the check.
The latest action prompt is marked missing in the prompt itself. Let me verify the current state of the task files and the latest action prompt.
Critical observation: the task files (protocol.md, asset_rule.yaml, registration.yaml) are all **stubs** with only template skeleton lines. There is no action prompt. The approach I executed in the previous config turn wrote files, but those changes don't appear to have been persisted. Let me verify the actual content state.
The previous session's configuration writes did not persist (or were cleared on a fast_pass transition). Now I'm in the **checking** stage with bare template stubs. The meta.yaml shows `status: active` and `sub_status: checking`, so status is correct.

Let me verify the assets referenced from the predecessor task and confirm what should be available.
The predecessor T-014 task has all artifacts and assets in place via symlinks. Note: T-014 symlinks point to "Current project protocol" (without `/0_overview.md`), and the file found in the protocol dir has the project protocol folder itself as target.

Let me check the T-014 inventory CSV and the 3_execution requirement for the current task.
Let me now retrieve the prompt template & configuration approach by looking at how the previous config turn was structured. I need to understand what the upstream action prompt will reference, and confirm the project state. Let me also check the API endpoint status.
I now have everything needed to do the check. Let me update todos and write the repaired configuration files.
