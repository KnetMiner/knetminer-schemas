

# Class: Expression Regulation Trait (RegulationTraitAssn) 


_A gene-to-trait association based on gene expression regulation._

__





URI: [motif:RegulationTraitAssn](https://knetminer.com/terms/motifs/motif-categories/RegulationTraitAssn)






```mermaid
 classDiagram
    class RegulationTraitAssn
    click RegulationTraitAssn href "../RegulationTraitAssn"
      HasGeneTraitAssociation <|-- RegulationTraitAssn
        click HasGeneTraitAssociation href "../HasGeneTraitAssociation"
      ExpressionRegulation <|-- RegulationTraitAssn
        click ExpressionRegulation href "../ExpressionRegulation"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [GeneExpression](GeneExpression.md) [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
        * [ExpressionRegulation](ExpressionRegulation.md)
            * **RegulationTraitAssn** [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | expression::regulation::genetics |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:RegulationTraitAssn |
| native | motif:RegulationTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RegulationTraitAssn
annotations:
  originalCategories:
    tag: originalCategories
    value: expression::regulation::genetics
description: 'A gene-to-trait association based on gene expression regulation.

  '
title: Expression Regulation Trait
notes:
- 'original category no: 2.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: ExpressionRegulation
mixins:
- HasGeneTraitAssociation

```
</details>

### Induced

<details>
```yaml
name: RegulationTraitAssn
annotations:
  originalCategories:
    tag: originalCategories
    value: expression::regulation::genetics
description: 'A gene-to-trait association based on gene expression regulation.

  '
title: Expression Regulation Trait
notes:
- 'original category no: 2.4'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: ExpressionRegulation
mixins:
- HasGeneTraitAssociation

```
</details>