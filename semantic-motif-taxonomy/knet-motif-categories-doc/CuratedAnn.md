

# Class: Direct Annotation (CuratedAnn) 


_Intra-species direct annotation, provided by a curator or expert._

__





URI: [motif:CuratedAnn](https://knetminer.com/terms/motifs/motif-categories/CuratedAnn)






```mermaid
 classDiagram
    class CuratedAnn
    click CuratedAnn href "../CuratedAnn"
      HasCuratedAnnotation <|-- CuratedAnn
        click HasCuratedAnnotation href "../HasCuratedAnnotation"
      IntraSpeciesAnnotation <|-- CuratedAnn
        click IntraSpeciesAnnotation href "../IntraSpeciesAnnotation"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [IntraSpeciesAnnotation](IntraSpeciesAnnotation.md) [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
        * **CuratedAnn** [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | direct::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:CuratedAnn |
| native | motif:CuratedAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CuratedAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::annotation
description: 'Intra-species direct annotation, provided by a curator or expert.

  '
title: Direct Annotation
notes:
- 'original category no: 1.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: IntraSpeciesAnnotation
mixins:
- HasCuratedAnnotation

```
</details>

### Induced

<details>
```yaml
name: CuratedAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::annotation
description: 'Intra-species direct annotation, provided by a curator or expert.

  '
title: Direct Annotation
notes:
- 'original category no: 1.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: IntraSpeciesAnnotation
mixins:
- HasCuratedAnnotation

```
</details>