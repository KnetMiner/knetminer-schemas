import unittest
import tempfile
import os
from io import StringIO
import sys
from unittest.mock import patch

from traverser_update_categs import extract_original_category_mapping, replace_categories_in_stdin


class TestExtractOriginalCategoryMapping(unittest.TestCase):
    
    def setUp(self):
        """Set up temporary files for testing"""
        self.temp_files = []
    
    def tearDown(self):
        """Clean up temporary files"""
        for temp_file in self.temp_files:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def create_temp_yaml(self, content):
        """Helper to create temporary YAML files"""
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False)
        temp_file.write(content)
        temp_file.close()
        self.temp_files.append(temp_file.name)
        return temp_file.name
    
    def test_extract_basic_mapping(self):
        """Test basic extraction of originalCategories mappings"""
        yaml_content = """
          classes:
            CoExpression:
              annotations:
                originalCategories: "expression::coexpression"
              description: "Co-expression relationship"
            
            GeneOntology:
              annotations:
                originalCategories: "ontology::go"
              description: "Gene Ontology term"
            
            RegularClass:
              description: "Class without originalCategories annotation"
          """
        
        temp_file = self.create_temp_yaml(yaml_content)
        result = extract_original_category_mapping(temp_file)
        
        expected = {
            "expression::coexpression": "CoExpression",
            "ontology::go": "GeneOntology"
        }
        
        self.assertEqual(result, expected)
    
    def test_extract_empty_classes(self):
        """Test handling of schema with no classes"""
        yaml_content = """
          name: test_schema
          description: "Test schema"
          """
        
        temp_file = self.create_temp_yaml(yaml_content)
        result = extract_original_category_mapping(temp_file)
        
        self.assertEqual(result, {})
    
    def test_extract_no_original_categories(self):
        """Test handling of classes without originalCategories annotations"""
        yaml_content = """
          classes:
            RegularClass1:
              description: "First regular class"
            
            RegularClass2:
              annotations:
                someOtherAnnotation: "value"
              description: "Second regular class"
          """
        
        temp_file = self.create_temp_yaml(yaml_content)
        result = extract_original_category_mapping(temp_file)
        
        self.assertEqual(result, {})
    
    def test_duplicate_original_category_same_class(self):
        """Test that duplicate originalCategories with same class name doesn't raise error"""
        yaml_content = """
          classes:
            CoExpression:
              annotations:
                originalCategories: "expression::coexpression, expression::coexpression"
              description: "Co-expression relationship"
          """
        
        temp_file = self.create_temp_yaml(yaml_content)
        # This should not raise an error
        result = extract_original_category_mapping(temp_file)
        
        expected = {"expression::coexpression": "CoExpression"}
        self.assertEqual(result, expected)
    
    def test_duplicate_original_category_different_class(self):
        """Test that duplicate originalCategories with different class names raises ValueError"""
        yaml_content = """
          classes:
            CoExpression:
              annotations:
                originalCategories: "expression::coexpression"
              description: "Co-expression relationship"
            
            AnotherClass:
              annotations:
                originalCategories: "expression::coexpression"
              description: "Another class with same originalCategories"
          """
        
        temp_file = self.create_temp_yaml(yaml_content)
        
        with self.assertRaises(ValueError) as context:
            extract_original_category_mapping(temp_file)
        
        self.assertIn("Duplicate originalCategory", str(context.exception))
        self.assertIn("expression::coexpression", str(context.exception))


class TestReplaceCategoriesInStdin(unittest.TestCase):
    
    def test_replace_single_occurrence(self):
        """Test replacing a single occurrence in a line"""
        input_text = "This is a line with expression::coexpression in it\n"
        mapping = {"expression::coexpression": "CoExpression"}
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                expected = "This is a line with CoExpression in it\n"
                self.assertEqual(result, expected)
    
    def test_replace_multiple_occurrences_same_line(self):
        """Test replacing multiple occurrences of the same category in one line"""
        input_text = "expression::coexpression and expression::coexpression again\n"
        mapping = {"expression::coexpression": "CoExpression"}
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                expected = "CoExpression and CoExpression again\n"
                self.assertEqual(result, expected)
    
    def test_replace_multiple_different_categories(self):
        """Test replacing multiple different categories in one line"""
        input_text = "We have expression::coexpression and ontology::go here\n"
        mapping = {
            "expression::coexpression": "CoExpression",
            "ontology::go": "GeneOntology"
        }
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                expected = "We have CoExpression and GeneOntology here\n"
                self.assertEqual(result, expected)
    
    def test_replace_multiple_lines(self):
        """Test replacing categories across multiple lines"""
        input_text = "Line 1: expression::coexpression\nLine 2: ontology::go\nLine 3: no categories\n"
        mapping = {
            "expression::coexpression": "CoExpression",
            "ontology::go": "GeneOntology"
        }
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                expected = "Line 1: CoExpression\nLine 2: GeneOntology\nLine 3: no categories\n"
                self.assertEqual(result, expected)
    
    def test_no_replacements_needed(self):
        """Test handling input with no categories to replace"""
        input_text = "This line has no categories to replace\nNeither does this one\n"
        mapping = {"expression::coexpression": "CoExpression"}
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                self.assertEqual(result, input_text)
    
    def test_empty_input(self):
        """Test handling empty input"""
        input_text = ""
        mapping = {"expression::coexpression": "CoExpression"}
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                self.assertEqual(result, "")
    
    def test_empty_mapping(self):
        """Test handling empty mapping dictionary"""
        input_text = "This has expression::coexpression in it\n"
        mapping = {}
        
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                replace_categories_in_stdin(mapping)
                
                result = mock_stdout.getvalue()
                self.assertEqual(result, input_text)


if __name__ == '__main__':
    unittest.main()
