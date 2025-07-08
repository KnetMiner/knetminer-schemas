import yaml
import sys
from typing import Dict


def extract_original_category_mapping(schema_file_path: str) -> Dict[str, str]:
	"""
	Scans LinkML schema class definitions and builds a dictionary mapping
	originalCategory annotation values to class names.
	
	Args:
		schema_file_path: Path to the LinkML YAML schema file
		
	Returns:
		Dictionary where keys are originalCategory values and values are class names
		
	Raises:
		ValueError: If duplicate originalCategory values are found with different class names
	"""
	
	# Load YAML file directly
	with open(schema_file_path, 'r') as f:
		schema_data = yaml.safe_load(f)
	
	# Dictionary to store the mapping
	original_category_mapping = {}
	
	# Get classes section
	classes = schema_data.get('classes', {})
	
	for class_name, class_def in classes.items():
		# Check if the class has annotations
		annotations = class_def.get('annotations', {})
		
		if 'originalCategory' in annotations:
			original_category_value = annotations['originalCategory']
			
			# Check for duplicates
			if original_category_value in original_category_mapping:
				existing_class = original_category_mapping[original_category_value]
				if existing_class != class_name:
					raise ValueError(
						f"Duplicate originalCategory '{original_category_value}' found: "
						f"'{existing_class}' and '{class_name}'"
					)
			
			# Add to mapping
			original_category_mapping[original_category_value] = class_name
	
	return original_category_mapping


def replace_categories_in_stdin(original2new_categs: Dict[str, str]) -> None:
	"""
	Reads stdin line by line and replaces occurrences of original category keys
	with their corresponding new category values.
	
	Args:
		original2new_categs: Dictionary mapping original categories to new class names
	"""
	
	for line in sys.stdin:
		# Process each line
		updated_line = line
		
		# Replace all occurrences of each original category with its new value
		for original_category, new_category in original2new_categs.items():
			updated_line = updated_line.replace(original_category, new_category)
		
		# Output the updated line
		sys.stdout.write(updated_line)


def replace_categories_from_schema(schema_file_path: str) -> None:
	"""
	Convenience function that extracts category mappings from a LinkML schema file
	and uses them to replace categories in stdin.
	
	Args:
		schema_file_path: Path to the LinkML YAML schema file
	"""
	
	# Extract the mapping from the schema file
	original2new_categs = extract_original_category_mapping(schema_file_path)
	
	# Use the mapping to replace categories in stdin
	replace_categories_in_stdin(original2new_categs)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python traverser-update-categs.py <schema_file_path>", file=sys.stderr)
		sys.exit(1)
	
	schema_file_path = sys.argv[1]
	replace_categories_from_schema(schema_file_path)