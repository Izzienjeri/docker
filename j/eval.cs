namespace abt_TestProject1;

using NUnit.Framework;
using NUnit.Framework.Constraints;
using System;
using System.Collections.Generic;
using System.Linq;

[TestFixture]
public class ABTestHelperTests
{
    [Test]
    public void Test_BasicFallbackUpdate()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 20),
            new ABTestVariant("B", 30),
            new ABTestVariant("Fallback", 0)
        };
        var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
        Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
        Assert.AreEqual(20, updatedVariants.First(v => v.VariationName == "A").Distribution); //check immutability
        Assert.AreEqual(30, updatedVariants.First(v => v.VariationName == "B").Distribution);
    		Assert.AreNotSame(variants, updatedVariants); //check for a new list
    }

    [Test]
    public void Test_EmptyVariantsList()
    {
        var variants = new List<IABTestVariant>();
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, "Fallback"), Throws.Exception);
    }

    [Test]
    public void Test_FallbackProviderNotFound()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 20),
            new ABTestVariant("B", 30)
        };
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, "Fallback"), Throws.Exception);
    }

    [Test]
    public void Test_FallbackAlreadyAt100()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 0),
            new ABTestVariant("Fallback", 100)
        };
        var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
        Assert.AreEqual(100, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
    }

    [Test]
    public void Test_NoOtherVariants()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("Fallback", 0)
        };
        var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
        Assert.AreEqual(100, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
    }

    [Test]
    public void Test_NullVariantsList()
    {
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(null, "Fallback"), Throws.Exception);
    }

    [Test]
    public void Test_NullFallbackProviderName()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 50),
            new ABTestVariant("Fallback", 50)
        };
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, null), Throws.Exception);
    }

    [Test]
    public void Test_EmptyFallbackProviderName()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 50),
            new ABTestVariant("Fallback", 50)
        };
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, ""), Throws.Exception);
    }

    [Test]
    public void Test_TotalPercentageExceeds100()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 60),
            new ABTestVariant("B", 50),
            new ABTestVariant("Fallback", 0)
        };
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, "Fallback"), Throws.Exception);
    }

	[Test]
	public void Test_MultipleFallbackVariants()
	{
		var variants = new List<IABTestVariant>
		{
			new ABTestVariant("A", 60),
			new ABTestVariant("Fallback", 20),
			new ABTestVariant("Fallback", 0)
		};
		Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, "Fallback"), Throws.Exception);
	}

    [Test]
    public void Test_FallbackNameWithDifferentCasing()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 20),
            new ABTestVariant("B", 30),
            new ABTestVariant("fallback", 0)
        };
        Assert.That(() => ABTestHelper.UpdateFallbackDistribution(variants, "Fallback"), Throws.Exception);
    }

    [Test]
    public void Test_MultipleVariantsWithSameName()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 20),
            new ABTestVariant("A", 30),
            new ABTestVariant("Fallback", 0)
        };
        var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
        Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
    }

        [Test]
    public void Test_VariantsWithZeroDistribution()
    {
        var variants = new List<IABTestVariant>
        {
            new ABTestVariant("A", 0),
            new ABTestVariant("B", 0),
            new ABTestVariant("Fallback", 0)
        };
        var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
         Assert.AreEqual(100, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
    }

	[Test]
	public void Test_FallbackAtBeginning()
	{
		var variants = new List<IABTestVariant>
		{
			new ABTestVariant("Fallback", 0),
			new ABTestVariant("A", 20),
			new ABTestVariant("B", 30)
		};
		var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
		Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
	}

	[Test]
	public void Test_FallbackInMiddle()
	{
		var variants = new List<IABTestVariant>
		{
			new ABTestVariant("A", 20),
			new ABTestVariant("Fallback", 0),
			new ABTestVariant("B", 30)
		};
		var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
		Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
	}

	[Test]
	public void Test_DistributionAlreadySumsTo100()
	{
		var variants = new List<IABTestVariant>
		{
			new ABTestVariant("A", 20),
			new ABTestVariant("B", 30),
			new ABTestVariant("Fallback", 50)
		};
		var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
		Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
	}

	[Test]
	public void Test_DistributionInitialSumAbove100()
	{
		var variants = new List<IABTestVariant>
		{
			new ABTestVariant("A", 20),
			new ABTestVariant("B", 30),
			new ABTestVariant("Fallback", 70)
		};
		var updatedVariants = ABTestHelper.UpdateFallbackDistribution(variants, "Fallback");
		Assert.AreEqual(50, updatedVariants.First(v => v.VariationName == "Fallback").Distribution);
	}
}
