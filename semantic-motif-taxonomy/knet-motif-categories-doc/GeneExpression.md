

# Class: Gene Expression (GeneExpression) 


_Associations of this type are related to gene expression, for instance because it's the mean used_

_to predict the function of a gene._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:GeneExpression](https://knetminer.com/terms/motifs/motif-categories/GeneExpression)






```mermaid
 classDiagram
    class GeneExpression
    click GeneExpression href "../GeneExpression"
      IntraSpeciesAssociation <|-- GeneExpression
        click IntraSpeciesAssociation href "../IntraSpeciesAssociation"
      SemanticMotifCategory <|-- GeneExpression
        click SemanticMotifCategory href "../SemanticMotifCategory"
      

      GeneExpression <|-- DifferentialExpression
        click DifferentialExpression href "../DifferentialExpression"
      GeneExpression <|-- CoExpression
        click CoExpression href "../CoExpression"
      GeneExpression <|-- ExpressionRegulation
        click ExpressionRegulation href "../ExpressionRegulation"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * **GeneExpression** [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
        * [DifferentialExpression](DifferentialExpression.md)
        * [CoExpression](CoExpression.md)
        * [ExpressionRegulation](ExpressionRegulation.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:GeneExpression |
| native | motif:GeneExpression |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneExpression
description: 'Associations of this type are related to gene expression, for instance
  because it''s the mean used

  to predict the function of a gene.

  '
title: Gene Expression
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>

### Induced

<details>
```yaml
name: GeneExpression
description: 'Associations of this type are related to gene expression, for instance
  because it''s the mean used

  to predict the function of a gene.

  '
title: Gene Expression
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>