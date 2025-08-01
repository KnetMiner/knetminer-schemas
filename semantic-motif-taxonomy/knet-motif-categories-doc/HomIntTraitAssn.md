

# Class: Homology Interaction Trait (HomIntTraitAssn) 


_A gene-to-trait association based on homology._

__





URI: [motif:HomIntTraitAssn](https://knetminer.com/terms/motifs/motif-categories/HomIntTraitAssn)






```mermaid
 classDiagram
    class HomIntTraitAssn
    click HomIntTraitAssn href "../HomIntTraitAssn"
      HasGeneTraitAssociation <|-- HomIntTraitAssn
        click HasGeneTraitAssociation href "../HasGeneTraitAssociation"
      HomologyInteraction <|-- HomIntTraitAssn
        click HomologyInteraction href "../HomologyInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [HomologyInteraction](HomologyInteraction.md)
        * **HomIntTraitAssn** [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | homint::genetics |




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
annotations:
  originalCategories:
    tag: originalCategories
    value: homint::genetics
description: 'A gene-to-trait association based on homology.

  '
title: Homology Interaction Trait
notes:
- 'original category no: 5.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- HasGeneTraitAssociation

```
</details>

### Induced

<details>
```yaml
name: HomIntTraitAssn
annotations:
  originalCategories:
    tag: originalCategories
    value: homint::genetics
description: 'A gene-to-trait association based on homology.

  '
title: Homology Interaction Trait
notes:
- 'original category no: 5.2'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- HasGeneTraitAssociation

```
</details>