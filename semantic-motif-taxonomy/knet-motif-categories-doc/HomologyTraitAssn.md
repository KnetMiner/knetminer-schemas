

# Class: Homology Trait (HomologyTraitAssn) 


_A gene-to-trait association based on homology._

__





URI: [motif:HomologyTraitAssn](https://knetminer.com/terms/motifs/motif-categories/HomologyTraitAssn)






```mermaid
 classDiagram
    class HomologyTraitAssn
    click HomologyTraitAssn href "../HomologyTraitAssn"
      HasGeneTraitAssociation <|-- HomologyTraitAssn
        click HasGeneTraitAssociation href "../HasGeneTraitAssociation"
      Homology <|-- HomologyTraitAssn
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * [Homology](Homology.md) [ [CrossSpeciesAssociation](CrossSpeciesAssociation.md)]
            * **HomologyTraitAssn** [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | phylogeny::homology::genetics |




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
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::genetics
description: 'A gene-to-trait association based on homology.

  '
title: Homology Trait
notes:
- 'original category no: 3.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasGeneTraitAssociation

```
</details>

### Induced

<details>
```yaml
name: HomologyTraitAssn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::genetics
description: 'A gene-to-trait association based on homology.

  '
title: Homology Trait
notes:
- 'original category no: 3.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasGeneTraitAssociation

```
</details>