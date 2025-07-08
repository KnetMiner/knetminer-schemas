

# Class: Gene-to-Trait Association via Sequence Similarity (SeqSimTraitAssn) 


_A gene-to-trait association based on sequence similarity._

__





URI: [motif:SeqSimTraitAssn](https://knetminer.com/terms/motifs/motif-categories/SeqSimTraitAssn)






```mermaid
 classDiagram
    class SeqSimTraitAssn
    click SeqSimTraitAssn href "../SeqSimTraitAssn"
      Gene2TraitAssociation <|-- SeqSimTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      SequenceSimilarity <|-- SeqSimTraitAssn
        click SequenceSimilarity href "../SequenceSimilarity"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [SequenceSimilarity](SequenceSimilarity.md) [ [AssociationStrength](AssociationStrength.md)]
                * **SeqSimTraitAssn** [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]



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
| self | motif:SeqSimTraitAssn |
| native | motif:SeqSimTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeqSimTraitAssn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::literature
description: 'A gene-to-trait association based on sequence similarity.

  '
title: Gene-to-Trait Association via Sequence Similarity
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- Gene2TraitAssociation

```
</details>

### Induced

<details>
```yaml
name: SeqSimTraitAssn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::similarity::literature
description: 'A gene-to-trait association based on sequence similarity.

  '
title: Gene-to-Trait Association via Sequence Similarity
notes:
- 'original category no: 4.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SequenceSimilarity
mixins:
- Gene2TraitAssociation

```
</details>