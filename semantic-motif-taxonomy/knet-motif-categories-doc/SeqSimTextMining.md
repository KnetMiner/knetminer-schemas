

# Class: Sequence Similarity Text Mining (SeqSimTextMining) 


_An association that represents a text mining annotation based on sequence similarity._

__





URI: [motif:SeqSimTextMining](https://knetminer.com/terms/motifs/motif-categories/SeqSimTextMining)






```mermaid
 classDiagram
    class SeqSimTextMining
    click SeqSimTextMining href "../SeqSimTextMining"
      HasTextMiningAnnotation <|-- SeqSimTextMining
        click HasTextMiningAnnotation href "../HasTextMiningAnnotation"
      SequenceSimilarity <|-- SeqSimTextMining
        click SequenceSimilarity href "../SequenceSimilarity"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * [SequenceSimilarity](SequenceSimilarity.md)
            * **SeqSimTextMining** [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



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
title: Sequence Similarity Text Mining
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- HasTextMiningAnnotation

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
title: Sequence Similarity Text Mining
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- HasTextMiningAnnotation

```
</details>