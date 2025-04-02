import os
import re
from extract_solution import extract_solution

llm_response =r'''
To implement a functional approach for updating the fallback provider's distribution, we can define the `UpdateFallbackDistribution` method to create and return a new list of `IABTestVariant` objects. The method will identify the fallback provider by name, calculate the remaining distribution percentage, and adjust the fallback provider's distribution accordingly.

Here's how you can implement this:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public static class ABTestHelper
{
    public static List<IABTestVariant> UpdateFallbackDistribution(IEnumerable<IABTestVariant> variants, string fallbackProviderName)
    {
        if (variants == null)
        {
            throw new ArgumentNullException(nameof(variants));
        }

        if (string.IsNullOrEmpty(fallbackProviderName))
        {
            throw new ArgumentNullException(nameof(fallbackProviderName));
        }

        // Calculate the total percentage of all variants
        int totalPercentage = variants.Sum(v => v.Distribution);

        // Calculate the remaining percentage to reach 100%
        int remainingPercentage = 100 - totalPercentage;

        // Create a new list to hold the updated variants
        var updatedVariants = new List<IABTestVariant>();

        foreach (var variant in variants)
        {
            if (variant.VariationName == fallbackProviderName)
            {
                // Update the distribution for the fallback provider
                var updatedFallback = new ABTestVariant(variant.VariationName, variant.Distribution + remainingPercentage);
                updatedVariants.Add(updatedFallback);
            }
            else
            {
                // Add the original variant to the updated list
                updatedVariants.Add(new ABTestVariant(variant.VariationName, variant.Distribution));
            }
        }

        return updatedVariants;
    }
}

public interface IABTestVariant
{
    string VariationName { get; }
    int Distribution { get; }
}

public class ABTestVariant : IABTestVariant
{
    public ABTestVariant(string variationName, int distribution)
    {
        if (string.IsNullOrEmpty(variationName))
        {
            throw new ArgumentNullException(nameof(variationName));
        }

        if (distribution < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(distribution), "Distribution must be non-negative.");
        }

        VariationName = variationName;
        Distribution = distribution;
    }

    public string VariationName { get; }
    public int Distribution { get; }
}
```

### Key Points

1. **Argument Validation:**
   - The method checks for null or empty inputs and throws appropriate exceptions to ensure robustness.

2. **Functional Style:**
   - The method processes the input list and returns a new list with updated variants, adhering to a functional programming style.

3. **Immutability:**
   - By creating new instances of `ABTestVariant` for both updated and unchanged variants, the original list remains unchanged, supporting immutability.

4. **Error Handling:**
   - Ensure that the `variants` collection and `fallbackProviderName` are valid to avoid runtime exceptions.

5. **Distribution Calculation:**
   - The method calculates the remaining percentage needed to make the total distribution equal to 100% and adjusts the fallback provider's distribution accordingly.

This implementation ensures that the `UpdateFallbackDistribution` method is clean, functional, and maintains immutability.
'''
    
try:
    extracted_blocks = extract_solution(llm_response)

    if not isinstance(extracted_blocks, list):
        raise ValueError("Expected extracted blocks to be a list of (language, code) tuples.")
    
    for index, (file_name, code) in enumerate(extracted_blocks):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(code)
        print(f"File '{file_name}' written successfully.")
except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")
except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")