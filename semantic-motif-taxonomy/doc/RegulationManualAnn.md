

# Class: Manual Annotation about Gene Expression Regulation (RegulationManualAnn) 


_An association that represents a manual annotation based on gene expression regulation. _

__





URI: [motif:RegulationManualAnn](https://knetminer.com/terms/motifs/motif-categories/RegulationManualAnn)






```mermaid
 classDiagram
    class RegulationManualAnn
    click RegulationManualAnn href "../RegulationManualAnn"
      ManualAnnotationMethod <|-- RegulationManualAnn
        click ManualAnnotationMethod href "../ManualAnnotationMethod"
      ExpressionRegulation <|-- RegulationManualAnn
        click ExpressionRegulation href "../ExpressionRegulation"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [GeneExpression](GeneExpression.md) [ [IntraSpecieAssociation](IntraSpecieAssociation.md)]
            * [ExpressionRegulation](ExpressionRegulation.md)
                * **RegulationManualAnn** [ [ManualAnnotationMethod](ManualAnnotationMethod.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | expression::regulation::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:RegulationManualAnn |
| native | motif:RegulationManualAnn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RegulationManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: expression::regulation::annotation
description: "An association that represents a manual annotation based on gene expression\
  \ regulation. \n"
title: Manual Annotation about Gene Expression Regulation
notes:
- 'original category no: 2.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: ExpressionRegulation
mixins:
- ManualAnnotationMethod

```
</details>

### Induced

<details>
```yaml
name: RegulationManualAnn
annotations:
  originalCategory:
    tag: originalCategory
    value: expression::regulation::annotation
description: "An association that represents a manual annotation based on gene expression\
  \ regulation. \n"
title: Manual Annotation about Gene Expression Regulation
notes:
- 'original category no: 2.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: ExpressionRegulation
mixins:
- ManualAnnotationMethod

```
</details>