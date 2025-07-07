

# Class: Manual Annotation about Sequence Similarity (SeqSimManualAnn) 


_An association that represents a manual annotation based on sequence similarity._

__





URI: [motif:SeqSimManualAnn](https://knetminer.com/terms/motifs/motif-categories/SeqSimManualAnn)






```mermaid
 classDiagram
    class SeqSimManualAnn
    click SeqSimManualAnn href "../SeqSimManualAnn"
      ManualAnnotation <|-- SeqSimManualAnn
        click ManualAnnotation href "../ManualAnnotation"
      SequenceSimilarity <|-- SeqSimManualAnn
        click SequenceSimilarity href "../SequenceSimilarity"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [SequenceSimilarity](SequenceSimilarity.md) [ [AssociationStrength](AssociationStrength.md)]
                * **SeqSimManualAnn** [ [ManualAnnotation](ManualAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | phylogeny::similarity::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:SeqSimManualAnn |
| native | motif:SeqSimManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeqSimManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::annotation
description: 'An association that represents a manual annotation based on sequence
  similarity.

  '
title: Manual Annotation about Sequence Similarity
notes:
- 'original category no: 4.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- ManualAnnotation

```
</details>

### Induced

<details>
```yaml
name: SeqSimManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::annotation
description: 'An association that represents a manual annotation based on sequence
  similarity.

  '
title: Manual Annotation about Sequence Similarity
notes:
- 'original category no: 4.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- ManualAnnotation

```
</details>