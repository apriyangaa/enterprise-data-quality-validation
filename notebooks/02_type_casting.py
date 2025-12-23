"""
Data type normalization pattern (casting to expected types)
"""

from pyspark.sql.functions import col

cast_df = validated_df.withColumn(
    "employee_id",
    col("employee_id").cast("string")
)

cast_df.display()
