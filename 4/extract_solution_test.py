"""Testing exatract_solution."""
import os
from extract_solution import extract_solution

llm_response = r'''
```python
import pandas as pd
from scipy.stats import pearsonr, spearmanr

def calculate_user_trait_correlations():
    """
    Calculate Pearson and Spearman correlations between dissemination order and user personality traits.

    Returns:
        pd.DataFrame: DataFrame containing the correlation results, indexed by userId and trait.
    """
    # Load the data again
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    user_personality = pd.read_csv('user_personality.csv')

    # Merge ratings with user personality scores
    ratings = ratings.merge(user_personality, on='userId')

    # Collect data, sort, and determine dissemination order (same logic as before)
    # For example, sort ratings and assign dissemination_order:
    ratings = ratings.sort_values(by=['userId', 'timestamp'])
    ratings['dissemination_order'] = ratings.groupby('userId').cumcount() + 1

    # Filter users with more than one rating to avoid ConstantInputWarning
    ratings = ratings[ratings.groupby('userId')['movieId'].transform('size') > 1]

    # Calculate correlation between dissemination order and personality scores
    correlations = {}
    for user_id, group in ratings.groupby('userId'):
        user_correlations = {}
        for trait in ['Extraversion', 'Agreeableness', 'Openness', 'Conscientiousness', 'Neuroticism']:
            pearson_corr, _ = pearsonr(group['dissemination_order'], group[trait])
            spearman_corr, _ = spearmanr(group['dissemination_order'], group[trait])
            user_correlations[trait] = {'Pearson': pearson_corr, 'Spearman': spearman_corr}
        correlations[user_id] = user_correlations

    # Print the correlation results for each user
    for user_id, corr_values in correlations.items():
        print(f"User {user_id}:")
        for trait, corr in corr_values.items():
            print(f"  {trait}: Pearson correlation = {corr['Pearson']}, Spearman correlation = {corr['Spearman']}")

    # Save the correlation results to a CSV file
    correlation_df = pd.DataFrame.from_dict({(i, j): correlations[i][j]
                                             for i in correlations.keys()
                                             for j in correlations[i].keys()},
                                            orient='index')
    correlation_df.to_csv('user_correlation_results.csv', index=True)

    return correlation_df

```

```python
import pandas as pd
from scipy.stats import pearsonr, spearmanr

def calculate_user_trait_correlations():
    """
    Calculate correlations between user personality traits and movie rating dissemination order.
    
    Returns:
        pd.DataFrame: DataFrame containing the correlation results, indexed by userId and trait.
    """
    # Load the data
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    user_personality = pd.read_csv('user_personality.csv')
    
    # Merge ratings with user personality scores
    ratings = ratings.merge(user_personality, on='userId')
    
    # Sort ratings by timestamp for each user
    ratings = ratings.sort_values(['userId', 'timestamp'])
    
    # Add dissemination order column
    ratings['dissemination_order'] = ratings.groupby('userId').cumcount() + 1
    
    # Filter users with more than one rating to avoid ConstantInputWarning
    ratings = ratings[ratings.groupby('userId')['movieId'].transform('size') > 1]
    
    # Initialize dictionary to store correlations
    correlations = {}
    
    # Calculate correlations for each user
    personality_traits = ['Extraversion', 'Agreeableness', 'Openness', 
                         'Conscientiousness', 'Neuroticism']
    
    for user_id, group in ratings.groupby('userId'):
        user_correlations = {}
        for trait in personality_traits:
            # Calculate Pearson correlation
            pearson_corr, p_value_pearson = pearsonr(group['dissemination_order'], 
                                                    group[trait])
            # Calculate Spearman correlation
            spearman_corr, p_value_spearman = spearmanr(group['dissemination_order'], 
                                                       group[trait])
            
            user_correlations[trait] = {
                'Pearson': pearson_corr,
                'Spearman': spearman_corr,
                'Pearson_p_value': p_value_pearson,
                'Spearman_p_value': p_value_spearman
            }
        correlations[user_id] = user_correlations
    
    # Create DataFrame from correlations dictionary
    correlation_rows = []
    for user_id, traits in correlations.items():
        for trait, corr_values in traits.items():
            row = {
                'userId': user_id,
                'trait': trait,
                'pearson_correlation': corr_values['Pearson'],
                'pearson_p_value': corr_values['Pearson_p_value'],
                'spearman_correlation': corr_values['Spearman'],
                'spearman_p_value': corr_values['Spearman_p_value']
            }
            correlation_rows.append(row)
    
    correlation_df = pd.DataFrame(correlation_rows)
    
    # Set multi-index for better organization
    correlation_df = correlation_df.set_index(['userId', 'trait'])
    
    # Save results to CSV
    correlation_df.to_csv('user_correlation_results.csv')
    
    # Print summary for each user
    for user_id, user_data in correlation_df.groupby('userId'):
        print(f"\nUser {user_id}:")
        for idx, row in user_data.iterrows():
            print(f"  {idx[1]}:")
            print(f"    Pearson correlation = {row['pearson_correlation']:.3f} "
                  f"(p-value = {row['pearson_p_value']:.3f})")
            print(f"    Spearman correlation = {row['spearman_correlation']:.3f} "
                  f"(p-value = {row['spearman_p_value']:.3f})")
    
    return correlation_df

```

'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples."
        )

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. "
                "Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
