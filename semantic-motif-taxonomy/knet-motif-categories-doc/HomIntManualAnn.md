

# Class: Manual Annotation about Homology Interaction (HomIntManualAnn) 


_An association that represents a manual annotation based on homology interaction._

__





URI: [motif:HomIntManualAnn](https://knetminer.com/terms/motifs/motif-categories/HomIntManualAnn)






```mermaid
 classDiagram
    class HomIntManualAnn
    click HomIntManualAnn href "../HomIntManualAnn"
      ManualAnnotation <|-- HomIntManualAnn
        click ManualAnnotation href "../ManualAnnotation"
      HomologyInteraction <|-- HomIntManualAnn
        click HomologyInteraction href "../HomologyInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * [HomologyInteraction](HomologyInteraction.md)
                    * **HomIntManualAnn** [ [ManualAnnotation](ManualAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomIntManualAnn |
| native | motif:HomIntManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomIntManualAnn
description: 'An association that represents a manual annotation based on homology
  interaction.

  '
title: Manual Annotation about Homology Interaction
notes:
- 'original category: 5.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- ManualAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomIntManualAnn
description: 'An association that represents a manual annotation based on homology
  interaction.

  '
title: Manual Annotation about Homology Interaction
notes:
- 'original category: 5.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- ManualAnnotation

```
</details>