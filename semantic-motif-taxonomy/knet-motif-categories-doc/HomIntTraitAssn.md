

# Class: Gene-to-Trait Association via homology (HomIntTraitAssn) 


_A gene-to-trait association based on homology._

__





URI: [motif:HomIntTraitAssn](https://knetminer.com/terms/motifs/motif-categories/HomIntTraitAssn)






```mermaid
 classDiagram
    class HomIntTraitAssn
    click HomIntTraitAssn href "../HomIntTraitAssn"
      Gene2TraitAssociation <|-- HomIntTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      HomologyInteraction <|-- HomIntTraitAssn
        click HomologyInteraction href "../HomologyInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * [HomologyInteraction](HomologyInteraction.md)
                    * **HomIntTraitAssn** [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomIntTraitAssn |
| native | motif:HomIntTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomIntTraitAssn
description: 'A gene-to-trait association based on homology.

  '
title: Gene-to-Trait Association via homology
notes:
- 'original category: 5.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- Gene2TraitAssociation

```
</details>

### Induced

<details>
```yaml
name: HomIntTraitAssn
description: 'A gene-to-trait association based on homology.

  '
title: Gene-to-Trait Association via homology
notes:
- 'original category: 5.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- Gene2TraitAssociation

```
</details>