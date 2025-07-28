# The KnetMiner Semantic Motif Taxonomy

This is a classification of semantic motif categories that KnetMiner uses to qualify semantic motif paths, gene/concept links that are found by semantic motif paths and anything similar or related to that.

The non-abstract classes that we define in the taxonomy are used by our [semantic motif traverser][10], to semantically characterise the queries that the traverser uses to find associations between genes and other concepts. Consequently, these categories are also used when the traverser stores the gene/concept associations achieved from the semantic motif paths, and which are those shown in the [end-user interface][20]

[10]: https://github.com/KnetMiner/knetminer-api/blob/main/doc/SemanticMotifs.md
[20]: https://api-dev.knetminer.com

## From here

* A [linkML-based][25] [formal specification][30]. 
	* This has an auto-generated [human-readable form][40], based on linkML tools.
* See [this GH issue][50], where we track discussions and design decisions about the development of the taxonomy.

[25]: https://linkml.io/linkml/intro/overview.html
[30]: knet-motif-categories.linkml.yaml
[40]: knet-motif-categories-doc/README.md
[50]: https://github.com/KnetMiner/knetminer-schemas/issues/1

