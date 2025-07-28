

# Class: Homology Annotation (HomologyManualAnn) 


_An association that represents a manual annotation based on homology._

__





URI: [motif:HomologyManualAnn](https://knetminer.com/terms/motifs/motif-categories/HomologyManualAnn)






```mermaid
 classDiagram
    class HomologyManualAnn
    click HomologyManualAnn href "../HomologyManualAnn"
      HasCuratedAnnotation <|-- HomologyManualAnn
        click HasCuratedAnnotation href "../HasCuratedAnnotation"
      Homology <|-- HomologyManualAnn
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * [Homology](Homology.md) [ [CrossSpeciesAssociation](CrossSpeciesAssociation.md)]
            * **HomologyManualAnn** [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | phylogeny::homology::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomologyManualAnn |
| native | motif:HomologyManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomologyManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::annotation
description: 'An association that represents a manual annotation based on homology.

  '
title: Homology Annotation
notes:
- 'original category no: 3.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasCuratedAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomologyManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::annotation
description: 'An association that represents a manual annotation based on homology.

  '
title: Homology Annotation
notes:
- 'original category no: 3.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasCuratedAnnotation

```
</details>