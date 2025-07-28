

# Class: Homoeology Annotation (HomoeologyAnn) 


_An association that represents a manual annotation based on homoeology._

__





URI: [motif:HomoeologyAnn](https://knetminer.com/terms/motifs/motif-categories/HomoeologyAnn)






```mermaid
 classDiagram
    class HomoeologyAnn
    click HomoeologyAnn href "../HomoeologyAnn"
      HasCuratedAnnotation <|-- HomoeologyAnn
        click HasCuratedAnnotation href "../HasCuratedAnnotation"
      Homoeology <|-- HomoeologyAnn
        click Homoeology href "../Homoeology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * [Homoeology](Homoeology.md) [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
            * **HomoeologyAnn** [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | phylogeny::homoeology::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomoeologyAnn |
| native | motif:HomoeologyAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomoeologyAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homoeology::annotation
description: 'An association that represents a manual annotation based on homoeology.

  '
title: Homoeology Annotation
notes:
- 'original category no: 3.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- HasCuratedAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomoeologyAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homoeology::annotation
description: 'An association that represents a manual annotation based on homoeology.

  '
title: Homoeology Annotation
notes:
- 'original category no: 3.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- HasCuratedAnnotation

```
</details>