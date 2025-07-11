

# Class: Manual Annotation about Physical Interaction (PhysInteractManualAnn) 


_An association that represents a manual annotation based on physical interaction._

__





URI: [motif:PhysInteractManualAnn](https://knetminer.com/terms/motifs/motif-categories/PhysInteractManualAnn)






```mermaid
 classDiagram
    class PhysInteractManualAnn
    click PhysInteractManualAnn href "../PhysInteractManualAnn"
      ManualAnnotationMethod <|-- PhysInteractManualAnn
        click ManualAnnotationMethod href "../ManualAnnotationMethod"
      PhysicalInteraction <|-- PhysInteractManualAnn
        click PhysicalInteraction href "../PhysicalInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [PhysicalInteraction](PhysicalInteraction.md)
            * **PhysInteractManualAnn** [ [ManualAnnotationMethod](ManualAnnotationMethod.md)]



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
| self | motif:PhysInteractManualAnn |
| native | motif:PhysInteractManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysInteractManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::annotation
description: 'An association that represents a manual annotation based on physical
  interaction.

  '
title: Manual Annotation about Physical Interaction
notes:
- 'original category no: 2.6'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- ManualAnnotationMethod

```
</details>

### Induced

<details>
```yaml
name: PhysInteractManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::annotation
description: 'An association that represents a manual annotation based on physical
  interaction.

  '
title: Manual Annotation about Physical Interaction
notes:
- 'original category no: 2.6'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- ManualAnnotationMethod

```
</details>