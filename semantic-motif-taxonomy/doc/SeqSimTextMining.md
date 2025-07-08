

# Class: Text Mining Annotation about Sequence Similarity (SeqSimTextMining) 


_An association that represents a text mining annotation based on sequence similarity._

__





URI: [motif:SeqSimTextMining](https://knetminer.com/terms/motifs/motif-categories/SeqSimTextMining)






```mermaid
 classDiagram
    class SeqSimTextMining
    click SeqSimTextMining href "../SeqSimTextMining"
      TextMiningAnnotationMethod <|-- SeqSimTextMining
        click TextMiningAnnotationMethod href "../TextMiningAnnotationMethod"
      SequenceSimilarity <|-- SeqSimTextMining
        click SequenceSimilarity href "../SequenceSimilarity"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [SequenceSimilarity](SequenceSimilarity.md) [ [AssociationStrength](AssociationStrength.md)]
                * **SeqSimTextMining** [ [TextMiningAnnotationMethod](TextMiningAnnotationMethod.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | phylogeny::similarity::literature |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:SeqSimTextMining |
| native | motif:SeqSimTextMining |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeqSimTextMining
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::literature
description: 'An association that represents a text mining annotation based on sequence
  similarity.

  '
title: Text Mining Annotation about Sequence Similarity
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- TextMiningAnnotationMethod

```
</details>

### Induced

<details>
```yaml
name: SeqSimTextMining
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::literature
description: 'An association that represents a text mining annotation based on sequence
  similarity.

  '
title: Text Mining Annotation about Sequence Similarity
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- TextMiningAnnotationMethod

```
</details>