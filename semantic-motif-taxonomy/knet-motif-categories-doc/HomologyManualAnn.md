

# Class: Manual Annotation about Homology (HomologyManualAnn) 


_An association that represents a manual annotation based on homology._

__





URI: [motif:HomologyManualAnn](https://knetminer.com/terms/motifs/motif-categories/HomologyManualAnn)






```mermaid
 classDiagram
    class HomologyManualAnn
    click HomologyManualAnn href "../HomologyManualAnn"
      ManualAnnotation <|-- HomologyManualAnn
        click ManualAnnotation href "../ManualAnnotation"
      Homology <|-- HomologyManualAnn
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * **HomologyManualAnn** [ [ManualAnnotation](ManualAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







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
description: 'An association that represents a manual annotation based on homology.

  '
title: Manual Annotation about Homology
notes:
- 'original category: 3.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- ManualAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomologyManualAnn
description: 'An association that represents a manual annotation based on homology.

  '
title: Manual Annotation about Homology
notes:
- 'original category: 3.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- ManualAnnotation

```
</details>