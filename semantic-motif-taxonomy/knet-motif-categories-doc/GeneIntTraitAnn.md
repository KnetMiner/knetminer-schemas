

# Class: Gene-Gene Interaction Trait (GeneIntTraitAnn) 


_A gene-to-trait association based on gene-gene interaction._

__





URI: [motif:GeneIntTraitAnn](https://knetminer.com/terms/motifs/motif-categories/GeneIntTraitAnn)






```mermaid
 classDiagram
    class GeneIntTraitAnn
    click GeneIntTraitAnn href "../GeneIntTraitAnn"
      HasGeneTraitAssociation <|-- GeneIntTraitAnn
        click HasGeneTraitAssociation href "../HasGeneTraitAssociation"
      GeneGeneInteraction <|-- GeneIntTraitAnn
        click GeneGeneInteraction href "../GeneGeneInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * [GeneGeneInteraction](GeneGeneInteraction.md)
            * **GeneIntTraitAnn** [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | interaction::genetic::genetics |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:GeneIntTraitAnn |
| native | motif:GeneIntTraitAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneIntTraitAnn
annotations:
  originalCategories:
    tag: originalCategories
    value: interaction::genetic::genetics
description: 'A gene-to-trait association based on gene-gene interaction.

  '
title: Gene-Gene Interaction Trait
notes:
- 'original category no: 2.10'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasGeneTraitAssociation

```
</details>

### Induced

<details>
```yaml
name: GeneIntTraitAnn
annotations:
  originalCategories:
    tag: originalCategories
    value: interaction::genetic::genetics
description: 'A gene-to-trait association based on gene-gene interaction.

  '
title: Gene-Gene Interaction Trait
notes:
- 'original category no: 2.10'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasGeneTraitAssociation

```
</details>