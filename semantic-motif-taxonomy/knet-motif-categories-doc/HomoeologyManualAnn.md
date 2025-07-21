

# Class: Manual Annotation about Homoeology (HomoeologyManualAnn) 


_An association that represents a manual annotation based on homoeology._

__





URI: [motif:HomoeologyManualAnn](https://knetminer.com/terms/motifs/motif-categories/HomoeologyManualAnn)






```mermaid
 classDiagram
    class HomoeologyManualAnn
    click HomoeologyManualAnn href "../HomoeologyManualAnn"
      ManualAnnotationMethod <|-- HomoeologyManualAnn
        click ManualAnnotationMethod href "../ManualAnnotationMethod"
      Homoeology <|-- HomoeologyManualAnn
        click Homoeology href "../Homoeology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homoeology](Homoeology.md) [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
                * **HomoeologyManualAnn** [ [ManualAnnotationMethod](ManualAnnotationMethod.md)]



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
| self | motif:HomoeologyManualAnn |
| native | motif:HomoeologyManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomoeologyManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homoeology::annotation
description: 'An association that represents a manual annotation based on homoeology.

  '
title: Manual Annotation about Homoeology
notes:
- 'original category no: 3.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- ManualAnnotationMethod

```
</details>

### Induced

<details>
```yaml
name: HomoeologyManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homoeology::annotation
description: 'An association that represents a manual annotation based on homoeology.

  '
title: Manual Annotation about Homoeology
notes:
- 'original category no: 3.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homoeology
mixins:
- ManualAnnotationMethod

```
</details>