

# Class: Gene-to-Trait Association via Homoeology (HomoeologyTraitAssn) 


_A gene-to-trait association based on homoeology._

__





URI: [motif:HomoeologyTraitAssn](https://knetminer.com/terms/motifs/motif-categories/HomoeologyTraitAssn)






```mermaid
 classDiagram
    class HomoeologyTraitAssn
    click HomoeologyTraitAssn href "../HomoeologyTraitAssn"
      Gene2TraitAssociation <|-- HomoeologyTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      Homoeology <|-- HomoeologyTraitAssn
        click Homoeology href "../Homoeology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homoeology](Homoeology.md) [ [IntraSpecieAssociation](IntraSpecieAssociation.md)]
                * **HomoeologyTraitAssn** [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomoeologyTraitAssn |
| native | motif:HomoeologyTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomoeologyTraitAssn
description: 'A gene-to-trait association based on homoeology.

  '
title: Gene-to-Trait Association via Homoeology
notes:
- 'original category: 3.5'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- Gene2TraitAssociation

```
</details>

### Induced

<details>
```yaml
name: HomoeologyTraitAssn
description: 'A gene-to-trait association based on homoeology.

  '
title: Gene-to-Trait Association via Homoeology
notes:
- 'original category: 3.5'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- Gene2TraitAssociation

```
</details>