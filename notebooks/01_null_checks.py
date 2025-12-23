"""
Null / mandatory field checks (enterprise data quality pattern)
"""

# Example dataframe assumed to be present
validated_df = df.filter("employee_id IS NOT NULL")

validated_df.display()
