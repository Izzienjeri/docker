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