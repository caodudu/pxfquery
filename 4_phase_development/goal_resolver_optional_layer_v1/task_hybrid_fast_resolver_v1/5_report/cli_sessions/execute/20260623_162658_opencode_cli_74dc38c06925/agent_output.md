This is the execution stage prompt. I need to actually deliver the T-033 hybrid fast resolver per protocol.md. Let me plan carefully since this is a real Python engineering task.
First, verify CyHex API + read upstream artifacts A-001 through A-004 to understand the resolver
Good. Now let me read the remaining A-003 guard code and the legacy QueryResolver to understand the
T-031 requires `pxfquery` importable package with `query.forward.ForwardQuery`. Let me check if T-024 workspace is installed
Different module path
Module path is `pxfquery.index.cellline_index`, `pxfquery.query.resolver`, etc. Let me probe the indexes and ForwardQuery
I have enough to build the resolver. Let me also check the bundle path for H5AD
Bundle is at `standard_resources/`. Let me locate H5AD files
Good. Now I have everything to write the resolver. Let me start with the implementation
