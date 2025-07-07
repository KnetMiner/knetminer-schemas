

# Class: Manual Annotation about Gene-Gene Interaction (GeneIntManualAnn) 


_An association that represents a manual annotation based on gene-gene interaction._

__





URI: [motif:GeneIntManualAnn](https://knetminer.com/terms/motifs/motif-categories/GeneIntManualAnn)






```mermaid
 classDiagram
    class GeneIntManualAnn
    click GeneIntManualAnn href "../GeneIntManualAnn"
      ManualAnnotation <|-- GeneIntManualAnn
        click ManualAnnotation href "../ManualAnnotation"
      GeneGeneInteraction <|-- GeneIntManualAnn
        click GeneGeneInteraction href "../GeneGeneInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [GeneGeneInteraction](GeneGeneInteraction.md)
            * **GeneIntManualAnn** [ [ManualAnnotation](ManualAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | interaction::genetic::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:GeneIntManualAnn |
| native | motif:GeneIntManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneIntManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::annotation
description: 'An association that represents a manual annotation based on gene-gene
  interaction.

  '
title: Manual Annotation about Gene-Gene Interaction
notes:
- 'original category no: 2.9'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- ManualAnnotation

```
</details>

### Induced

<details>
```yaml
name: GeneIntManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::annotation
description: 'An association that represents a manual annotation based on gene-gene
  interaction.

  '
title: Manual Annotation about Gene-Gene Interaction
notes:
- 'original category no: 2.9'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- ManualAnnotation

```
</details>