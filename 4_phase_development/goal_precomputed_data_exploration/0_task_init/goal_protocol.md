# Precomputed data exploration — Protocol

This development goal is for understanding and using PxFquery precomputed data assets.

Tasks under this goal should map what data already exists, how raw or intermediate CMAP/LINCS assets connect to precomputed functional matrices, what metadata and indexes make those matrices interpretable, and what existing tables or figures can support manuscript-grade visualization.

This goal is separate from algorithm run-through review and algorithm code development. It may inspect data, compute bounded metadata summaries, design figure resources, and later create data exploration or visualization outputs. It should not repair algorithm code or make broad package-readiness claims.

Expected work areas include:

- inventory of functional matrices, source AnnData objects, metadata tables, query indexes, embeddings, result tables, and figure files;
- explanation of the precomputation chain and how matrix values should be interpreted;
- data coverage summaries for perturbation type, cell line, gene/drug, function set, and evidence availability;
- identification of analysis-ready tables and figure-ready resources;
- design of candidate manuscript figures for data scale, matrix construction, coverage, sparsity, and example functional landscapes.
