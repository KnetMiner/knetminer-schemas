

# Class: Gene-to-Trait Association via homology (HomologyTraitAssn) 


_A gene-to-trait association based on homology._

__





URI: [motif:HomologyTraitAssn](https://knetminer.com/terms/motifs/motif-categories/HomologyTraitAssn)






```mermaid
 classDiagram
    class HomologyTraitAssn
    click HomologyTraitAssn href "../HomologyTraitAssn"
      Gene2TraitAssociation <|-- HomologyTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      Homology <|-- HomologyTraitAssn
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * **HomologyTraitAssn** [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomologyTraitAssn |
| native | motif:HomologyTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomologyTraitAssn
description: 'A gene-to-trait association based on homology.

  '
title: Gene-to-Trait Association via homology
notes:
- 'original category: 3.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- Gene2TraitAssociation

```
</details>

### Induced

<details>
```yaml
name: HomologyTraitAssn
description: 'A gene-to-trait association based on homology.

  '
title: Gene-to-Trait Association via homology
notes:
- 'original category: 3.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- Gene2TraitAssociation

```
</details>