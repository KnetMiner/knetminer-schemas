

# Class: Intra-species Gene-Trait Association (IntraTraitAssn) 


_A gene-trait association that is established with information and methods within the same species_

_as the association target gene (eg through GWAS experiments)._

__





URI: [motif:IntraTraitAssn](https://knetminer.com/terms/motifs/motif-categories/IntraTraitAssn)






```mermaid
 classDiagram
    class IntraTraitAssn
    click IntraTraitAssn href "../IntraTraitAssn"
      IntraSpeciesAssociation <|-- IntraTraitAssn
        click IntraSpeciesAssociation href "../IntraSpeciesAssociation"
      Gene2TraitAssociation <|-- IntraTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Gene2PhenotypeAssociation](Gene2PhenotypeAssociation.md)
            * [Gene2TraitAssociation](Gene2TraitAssociation.md)
                * **IntraTraitAssn** [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | direct::genetics |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:IntraTraitAssn |
| native | motif:IntraTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntraTraitAssn
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::genetics
description: 'A gene-trait association that is established with information and methods
  within the same species

  as the association target gene (eg through GWAS experiments).

  '
title: Intra-species Gene-Trait Association
notes:
- 'original category no: 1.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Gene2TraitAssociation
mixins:
- IntraSpeciesAssociation

```
</details>

### Induced

<details>
```yaml
name: IntraTraitAssn
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::genetics
description: 'A gene-trait association that is established with information and methods
  within the same species

  as the association target gene (eg through GWAS experiments).

  '
title: Intra-species Gene-Trait Association
notes:
- 'original category no: 1.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Gene2TraitAssociation
mixins:
- IntraSpeciesAssociation

```
</details>