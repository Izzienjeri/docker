
public static class ABTestHelper
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
