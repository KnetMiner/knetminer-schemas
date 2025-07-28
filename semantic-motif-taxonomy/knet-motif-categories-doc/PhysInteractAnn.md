

# Class: Physical Interaction Annotation (PhysInteractAnn) 


_A curated annotation about physical interaction._

__





URI: [motif:PhysInteractAnn](https://knetminer.com/terms/motifs/motif-categories/PhysInteractAnn)






```mermaid
 classDiagram
    class PhysInteractAnn
    click PhysInteractAnn href "../PhysInteractAnn"
      HasCuratedAnnotation <|-- PhysInteractAnn
        click HasCuratedAnnotation href "../HasCuratedAnnotation"
      PhysicalInteraction <|-- PhysInteractAnn
        click PhysicalInteraction href "../PhysicalInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * [PhysicalInteraction](PhysicalInteraction.md)
            * **PhysInteractAnn** [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | interaction::physical::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:PhysInteractAnn |
| native | motif:PhysInteractAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysInteractAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::annotation
description: 'A curated annotation about physical interaction.

  '
title: Physical Interaction Annotation
notes:
- 'original category no: 2.6'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- HasCuratedAnnotation

```
</details>

### Induced

<details>
```yaml
name: PhysInteractAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::annotation
description: 'A curated annotation about physical interaction.

  '
title: Physical Interaction Annotation
notes:
- 'original category no: 2.6'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- HasCuratedAnnotation

```
</details>