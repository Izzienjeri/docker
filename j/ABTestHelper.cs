
using System.Collections.Generic;
using System.Linq;

public interface IABTestVariant
{
  string VariationName { get; }
  int Distribution { get; }

  // required for Claude 3.5 Sonnet
  ABTestVariant UpdateDistribution(string variationName, int distribution);
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

	// required for Claude 3.5 Sonnet
    public ABTestVariant UpdateDistribution(string variationName, int distribution)
    {
        return new ABTestVariant(variationName, distribution);
    }

    public string VariationName { get; }
    public int Distribution { get; }
}



public static class ABTestHelper_gemini
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

        List<IABTestVariant> updatedVariants = variants.ToList(); // Create a mutable copy

        int totalPercentage = updatedVariants.Sum(v => v.Distribution);

        if (totalPercentage > 100)
        {
            throw new InvalidOperationException("Total distribution exceeds 100%.");
        }

        int remainingPercentage = 100 - totalPercentage;

        // Find the fallback provider
        int fallbackIndex = updatedVariants.FindIndex(v => string.Equals(v.VariationName, fallbackProviderName, StringComparison.OrdinalIgnoreCase));

        if (fallbackIndex == -1)
        {
            throw new ArgumentException($"Fallback provider with name '{fallbackProviderName}' not found.", nameof(fallbackProviderName));
        }

        //Update fallback variant
        IABTestVariant oldFallbackVariant = updatedVariants[fallbackIndex];
        IABTestVariant updatedFallbackVariant = new ABTestVariant(oldFallbackVariant.VariationName, oldFallbackVariant.Distribution + remainingPercentage);
        updatedVariants[fallbackIndex] = updatedFallbackVariant;

        return updatedVariants;
    }
}


public static class ABTestHelper_4o
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



public static class ABTestHelper_sonnet
{
    public static List<IABTestVariant> UpdateFallbackDistribution(
        IEnumerable<IABTestVariant> variants, 
        string fallbackProviderName)
    {
        var variantsList = variants.ToList();
        var totalPercentage = variantsList
            .Where(v => v.VariationName != fallbackProviderName)
            .Sum(v => v.Distribution);
            
        return variantsList
            .Select(variant => 
                variant.VariationName == fallbackProviderName
                    ? variant.UpdateDistribution(
                        variant.VariationName, 
                        100 - totalPercentage)
                    : variant)
            .ToList();
    }
}


public static class ABTestHelper_passes
{
    public static List<IABTestVariant> UpdateFallbackDistribution(
        IEnumerable<IABTestVariant> variants, 
        string fallbackProviderName)
    {
        var containsUniqueFallbackProvider = variants.ToList().FindAll(v => v.VariationName == fallbackProviderName).Count == 1;
        if (!containsUniqueFallbackProvider)
        {
          throw new ArgumentException("List should contain a unique entry for the fallback provider");
        }

        var totalPercentage = variants
            .Where(v => v.VariationName != fallbackProviderName)
            .Sum(v => v.Distribution);
            
        return variants
            .Select(variant => 
                variant.VariationName == fallbackProviderName
                    ? variant.UpdateDistribution(
                        variant.VariationName, 
                        100 - totalPercentage)
                    : variant)
            .ToList();
    }
}

