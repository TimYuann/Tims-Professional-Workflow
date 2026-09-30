# M3 case 2 · B/C authoring input

This is an offline exercise about a viewer whose overview and case details are read at different moments. The underlying case store can change between those reads.

Define the externally observable behavior and the domain meaning needed for a coherent view during one user interaction, including what may be observed by a later interaction. Keep the contract small enough to test and state the important example/exception.

The fixture contains `state_store`, `page_summary`, `turn` and `case_reader` modules. Read them as evidence of the current system. This task does not ask you to place responsibilities in those modules, design an interface, name a recall route, or choose an implementation. Those are later judgments. Keep the result scoped to this synthetic fixture; do not imply business rules for UCBIP or another product.

No external service, persistent migration, production data, or network access is part of the exercise.
