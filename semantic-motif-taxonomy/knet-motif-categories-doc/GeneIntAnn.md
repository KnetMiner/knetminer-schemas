

# Class: Gene-Gene Interaction Annotation (GeneIntAnn) 


_An association that represents a manual annotation based on gene-gene interaction._

__





URI: [motif:GeneIntAnn](https://knetminer.com/terms/motifs/motif-categories/GeneIntAnn)






```mermaid
 classDiagram
    class GeneIntAnn
    click GeneIntAnn href "../GeneIntAnn"
      HasCuratedAnnotation <|-- GeneIntAnn
        click HasCuratedAnnotation href "../HasCuratedAnnotation"
      GeneGeneInteraction <|-- GeneIntAnn
        click GeneGeneInteraction href "../GeneGeneInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * [GeneGeneInteraction](GeneGeneInteraction.md)
            * **GeneIntAnn** [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]



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
| self | motif:GeneIntAnn |
| native | motif:GeneIntAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneIntAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::annotation
description: 'An association that represents a manual annotation based on gene-gene
  interaction.

  '
title: Gene-Gene Interaction Annotation
notes:
- 'original category no: 2.9'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasCuratedAnnotation

```
</details>

### Induced

<details>
```yaml
name: GeneIntAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::annotation
description: 'An association that represents a manual annotation based on gene-gene
  interaction.

  '
title: Gene-Gene Interaction Annotation
notes:
- 'original category no: 2.9'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasCuratedAnnotation

```
</details>