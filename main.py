"""
Project 01: Chicago Socioeconomic Data Analysis with SQLite
============================================================
This script demonstrates SQLite database operations, SQL queries, 
and data analysis using Python and pandas.

Original notebooks: 4 notebooks combined
- DB0201EN-Week3-1-3-SQLmagic-SQlite-v2.ipynb
- DB0201EN-Week3-1-4-Analyzing-SQLite-v2.ipynb
- DB0201EN-Week4-1-1-RealDataPractice-v5-sqlite-Learner-v2(Edited).ipynb
- Week4-Insert-Update-SQLite-v2.ipynb

Author: Data Analysis Portfolio
"""

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================================
# SECTION 1: SQLite Database Creation and Basic Operations
# ================================================================================

def create_sample_database():
    """Create a sample SQLite database with international student test scores."""
    conn = sqlite3.connect("SQLiteMagic.db")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS INTERNATIONAL_STUDENT_TEST_SCORES (
            country VARCHAR(50),
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            test_score INT
        )
    """)
    
    # Sample data
    sample_data = [
        ('United States', 'Marshall', 'Bernadot', 54),
        ('Ghana', 'Celinda', 'Malkin', 51),
        ('Ukraine', 'Guillermo', 'Furze', 53),
        ('Greece', 'Aharon', 'Tunnow', 48),
        ('Russia', 'Bail', 'Goodwin', 46),
        ('Poland', 'Cole', 'Winteringham', 49),
        ('Sweden', 'Emlyn', 'Erricker', 55),
        ('Russia', 'Cathee', 'Sivewright', 49),
        ('China', 'Barny', 'Ingerson', 57),
        ('Uganda', 'Sharla', 'Papaccio', 55),
        ('China', 'Stella', 'Youens', 51),
        ('Poland', 'Julio', 'Buesden', 48),
        ('United States', 'Tiffie', 'Cosely', 58),
        ('Poland', 'Auroora', 'Stiffell', 45),
        ('China', 'Clarita', 'Huet', 52),
        ('Poland', 'Shannon', 'Goulden', 45),
        ('Philippines', 'Emylee', 'Privost', 50),
        ('France', 'Madelina', 'Burk', 49),
        ('China', 'Saunderson', 'Root', 58),
        ('Indonesia', 'Bo', 'Waring', 55),
        ('China', 'Hollis', 'Domotor', 45),
        ('Russia', 'Robbie', 'Collip', 46),
        ('Philippines', 'Davon', 'Donisi', 46),
        ('China', 'Cristabel', 'Radeliffe', 48),
        ('China', 'Wallis', 'Bartleet', 58),
        ('Moldova', 'Arleen', 'Stailey', 38),
        ('Ireland', 'Mendel', 'Grumble', 58),
        ('China', 'Sallyann', 'Exley', 51),
        ('Mexico', 'Kain', 'Swaite', 46),
        ('Indonesia', 'Alonso', 'Bulteel', 45),
        ('Armenia', 'Anatol', 'Tankus', 51),
        ('Indonesia', 'Coralyn', 'Dawkins', 48),
        ('China', 'Deanne', 'Edwinson', 45),
        ('China', 'Georgiana', 'Epple', 51),
        ('Portugal', 'Bartlet', 'Breese', 56),
        ('Azerbaijan', 'Idalina', 'Lukash', 50),
        ('France', 'Livvie', 'Flory', 54),
        ('Malaysia', 'Nonie', 'Borit', 48),
        ('Indonesia', 'Clio', 'Mugg', 47),
        ('Brazil', 'Westley', 'Measor', 48),
        ('Philippines', 'Katrinka', 'Sibbert', 51),
        ('Poland', 'Valentia', 'Mounch', 50),
        ('Norway', 'Sheilah', 'Hedditch', 53),
        ('Papua New Guinea', 'Itch', 'Jubb', 50),
        ('Latvia', 'Stesha', 'Garnson', 53),
        ('Canada', 'Cristionna', 'Wadmore', 46),
        ('China', 'Lianna', 'Gatward', 43),
        ('Guatemala', 'Tanney', 'Vials', 48),
        ('France', 'Alma', 'Zavittieri', 44),
        ('China', 'Alvira', 'Tamas', 50),
        ('United States', 'Shanon', 'Peres', 45),
        ('Sweden', 'Maisey', 'Lynas', 53),
        ('Indonesia', 'Kip', 'Hothersall', 46),
        ('China', 'Cash', 'Landis', 48),
        ('Panama', 'Kennith', 'Digance', 45),
        ('China', 'Ulberto', 'Riggeard', 48),
        ('Switzerland', 'Judy', 'Gilligan', 49),
        ('Philippines', 'Tod', 'Trevaskus', 52),
        ('Brazil', 'Herold', 'Heggs', 44),
        ('Latvia', 'Verney', 'Note', 50),
        ('Poland', 'Temp', 'Ribey', 50),
        ('China', 'Conroy', 'Egdal', 48),
        ('Japan', 'Gabie', 'Alessandone', 47),
    ]
    
    cursor.executemany(
        "INSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES (country, first_name, last_name, test_score) VALUES (?, ?, ?, ?)",
        sample_data
    )
    
    conn.commit()
    conn.close()
    print("Sample database created: SQLiteMagic.db")

def query_with_pandas():
    """Query the database using pandas."""
    conn = sqlite3.connect("SQLiteMagic.db")
    
    # Read entire table
    df = pd.read_sql_query("SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES", conn)
    print(f"Total records: {len(df)}")
    print(df.head(10))
    
    # Query with filtering
    df_china = pd.read_sql_query(
        "SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES WHERE country = 'China'", 
        conn
    )
    print(f"\nChinese students: {len(df_china)}")
    print(df_china)
    
    # Aggregation query
    df_stats = pd.read_sql_query("""
        SELECT country, COUNT(*) as student_count, AVG(test_score) as avg_score
        FROM INTERNATIONAL_STUDENT_TEST_SCORES
        GROUP BY country
        ORDER BY avg_score DESC
    """, conn)
    print("\nCountry statistics:")
    print(df_stats)
    
    conn.close()
    return df

def demonstrate_sql_operations():
    """Demonstrate various SQL operations."""
    conn = sqlite3.connect("SQLiteMagic.db")
    cursor = conn.cursor()
    
    # UPDATE example
    cursor.execute("""
        UPDATE INTERNATIONAL_STUDENT_TEST_SCORES
        SET test_score = test_score + 1
        WHERE country = 'United States'
    """)
    print(f"Updated {cursor.rowcount} rows for United States")
    
    # DELETE example
    cursor.execute("""
        DELETE FROM INTERNATIONAL_STUDENT_TEST_SCORES
        WHERE test_score < 45
    """)
    print(f"Deleted {cursor.rowcount} rows with score < 45")
    
    conn.commit()
    conn.close()

# ================================================================================
# SECTION 2: Chicago Socioeconomic Data Analysis
# ================================================================================

def analyze_chicago_data():
    """Analyze Chicago socioeconomic data."""
    # Note: In original notebook, data was loaded from a CSV file
    # Here we create sample data for demonstration
    
    # Sample Chicago socioeconomic data structure
    chicago_data = {
        'community_area': list(range(1, 78)),
        'community_name': [f'Community_{i}' for i in range(1, 78)],
        'population': np.random.randint(10000, 100000, 77),
        'per_capita_income': np.random.randint(15000, 80000, 77),
        'hardship_index': np.random.randint(1, 100, 77),
        'unemployment_rate': np.random.uniform(2, 20, 77),
        'below_poverty': np.random.uniform(5, 40, 77),
        'crowded_housing': np.random.uniform(1, 15, 77),
        'dependency': np.random.uniform(20, 50, 77),
        'no_diploma': np.random.uniform(5, 30, 77),
    }
    
    df = pd.DataFrame(chicago_data)
    
    print("Chicago Socioeconomic Data Analysis")
    print("=" * 50)
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nBasic Statistics:")
    print(df.describe())
    
    # Correlation analysis
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    print("\nCorrelation with Hardship Index:")
    if 'hardship_index' in corr_matrix.columns:
        print(corr_matrix['hardship_index'].sort_values(ascending=False))
    
    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Hardship index distribution
    axes[0, 0].hist(df['hardship_index'], bins=20, edgecolor='black', alpha=0.7)
    axes[0, 0].set_title('Hardship Index Distribution')
    axes[0, 0].set_xlabel('Hardship Index')
    axes[0, 0].set_ylabel('Frequency')
    
    # Per capita income vs Hardship
    axes[0, 1].scatter(df['per_capita_income'], df['hardship_index'], alpha=0.6)
    axes[0, 1].set_title('Per Capita Income vs Hardship Index')
    axes[0, 1].set_xlabel('Per Capita Income ($)')
    axes[0, 1].set_ylabel('Hardship Index')
    
    # Unemployment vs Hardship
    axes[1, 0].scatter(df['unemployment_rate'], df['hardship_index'], alpha=0.6, color='orange')
    axes[1, 0].set_title('Unemployment Rate vs Hardship Index')
    axes[1, 0].set_xlabel('Unemployment Rate (%)')
    axes[1, 0].set_ylabel('Hardship Index')
    
    # Correlation heatmap
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
                ax=axes[1, 1], cbar_kws={'shrink': 0.8})
    axes[1, 1].set_title('Correlation Matrix')
    
    plt.tight_layout()
    plt.savefig('chicago_analysis.png', dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'chicago_analysis.png'")
    plt.close()
    
    return df

# ================================================================================
# MAIN EXECUTION
# ================================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PROJECT 01: CHICAGO SOCIOECONOMIC SQLITE ANALYSIS")
    print("=" * 60)
    
    # Section 1: SQLite basics
    print("\n[1] Creating sample SQLite database...")
    create_sample_database()
    
    print("\n[2] Querying with pandas...")
    df = query_with_pandas()
    
    print("\n[3] Demonstrating SQL operations...")
    demonstrate_sql_operations()
    
    # Section 2: Chicago data analysis
    print("\n[4] Analyzing Chicago socioeconomic data...")
    chicago_df = analyze_chicago_data()
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
