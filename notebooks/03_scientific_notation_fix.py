"""
Fix scientific notation / formatting issues for numeric fields
"""

from pyspark.sql.functions import format_number, col

clean_df = cast_df.withColumn(
    "compensation_amount_clean",
    format_number(col("compensation_amount"), 2)
)

clean_df.display()
