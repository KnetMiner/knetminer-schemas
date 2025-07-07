

# Class: Sequence Similarity-based Association (SequenceSimilarity) 


_Associations of this type are more speculative than homoeology or homology, since sequence similarity_

_does not guarantee a shared evolutionary origin or function._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:SequenceSimilarity](https://knetminer.com/terms/motifs/motif-categories/SequenceSimilarity)






```mermaid
 classDiagram
    class SequenceSimilarity
    click SequenceSimilarity href "../SequenceSimilarity"
      AssociationStrength <|-- SequenceSimilarity
        click AssociationStrength href "../AssociationStrength"
      Phylogeny <|-- SequenceSimilarity
        click Phylogeny href "../Phylogeny"
      

      SequenceSimilarity <|-- SeqSimManualAnn
        click SeqSimManualAnn href "../SeqSimManualAnn"
      SequenceSimilarity <|-- SeqSimTraitAssn
        click SeqSimTraitAssn href "../SeqSimTraitAssn"
      SequenceSimilarity <|-- SeqSimTextMining
        click SeqSimTextMining href "../SeqSimTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * **SequenceSimilarity** [ [AssociationStrength](AssociationStrength.md)]
                * [SeqSimManualAnn](SeqSimManualAnn.md) [ [ManualAnnotation](ManualAnnotation.md)]
                * [SeqSimTraitAssn](SeqSimTraitAssn.md) [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]
                * [SeqSimTextMining](SeqSimTextMining.md) [ [TextMiningAnnotation](TextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| associationStrength | 4 |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:SequenceSimilarity |
| native | motif:SequenceSimilarity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SequenceSimilarity
annotations:
  associationStrength:
    tag: associationStrength
    value: 4
description: 'Associations of this type are more speculative than homoeology or homology,
  since sequence similarity

  does not guarantee a shared evolutionary origin or function.

  '
title: Sequence Similarity-based Association
notes:
- 'original category no: Tier 4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Phylogeny
abstract: true
mixins:
- AssociationStrength

```
</details>

### Induced

<details>
```yaml
name: SequenceSimilarity
annotations:
  associationStrength:
    tag: associationStrength
    value: 4
description: 'Associations of this type are more speculative than homoeology or homology,
  since sequence similarity

  does not guarantee a shared evolutionary origin or function.

  '
title: Sequence Similarity-based Association
notes:
- 'original category no: Tier 4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Phylogeny
abstract: true
mixins:
- AssociationStrength

```
</details>