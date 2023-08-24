
- Initialize the `track` with the placeholder value `-100000`and a `length` with `0`
- Inside a loop, if you encounter with a new distinct value (that differs from the last appended track value)
- You assign that unique value at the pointer `length` and increment it by 1 and append that value into the new `track`
- If you encounter with the same value twice. Repeat the point 3.
- If the value occurs for more than 2 times, `length` will not be incremented until a new value will not be found.