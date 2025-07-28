

# Class: Expression Regulation (ExpressionRegulation) 


_Association about the regulation of the gene expression of a gene done by another gene, protein or_

_biological entity._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:ExpressionRegulation](https://knetminer.com/terms/motifs/motif-categories/ExpressionRegulation)






```mermaid
 classDiagram
    class ExpressionRegulation
    click ExpressionRegulation href "../ExpressionRegulation"
      GeneExpression <|-- ExpressionRegulation
        click GeneExpression href "../GeneExpression"
      

      ExpressionRegulation <|-- RegulationAnn
        click RegulationAnn href "../RegulationAnn"
      ExpressionRegulation <|-- RegulationTraitAssn
        click RegulationTraitAssn href "../RegulationTraitAssn"
      ExpressionRegulation <|-- RegulationTextMining
        click RegulationTextMining href "../RegulationTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [GeneExpression](GeneExpression.md) [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
        * **ExpressionRegulation**
            * [RegulationAnn](RegulationAnn.md) [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]
            * [RegulationTraitAssn](RegulationTraitAssn.md) [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]
            * [RegulationTextMining](RegulationTextMining.md) [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:ExpressionRegulation |
| native | motif:ExpressionRegulation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExpressionRegulation
description: 'Association about the regulation of the gene expression of a gene done
  by another gene, protein or

  biological entity.

  '
title: Expression Regulation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneExpression
abstract: true

```
</details>

### Induced

<details>
```yaml
name: ExpressionRegulation
description: 'Association about the regulation of the gene expression of a gene done
  by another gene, protein or

  biological entity.

  '
title: Expression Regulation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneExpression
abstract: true

```
</details>