import axios from "axios";
import { toast } from "react-toastify";
import { handleFormSubmit } from "./solution.mjs";
jest.mock("axios");
jest.mock("react-toastify", () => ({
  toast: {
    success: jest.fn(),
    error: jest.fn(),
  },
}));

describe("handleFormSubmit", () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should handle successful API response", async () => {
    axios.post.mockResolvedValue({
      data: { status: true, message: "Item created successfully" },
    });

    const values = {
      ipd_enrollment_id: 1,
      price_per_item: 100,
      quantity: 2,
      ipd_bill_category_id: "cat1",
      ipd_bill_item_id: "item1",
      amount: 200,
    };

    const resetForm = jest.fn();
    const formikHelpers = { resetForm };

    await handleFormSubmit(values, formikHelpers);

    expect(axios.post).toHaveBeenCalledWith(
      "/api/doctor/ipd_enrollement_bill_items/create",
      { ...values, ipd_enrollment_id: 123 },
      { Authorization: "Bearer token" }
    );

    expect(toast.success).toHaveBeenCalledWith(
      "Item created successfully",
      expect.any(Object)
    );

    expect(resetForm).toHaveBeenCalled();
  });

  it("should handle failed API response", async () => {
    axios.post.mockResolvedValue({
      data: { status: null, message: "Failed to create item" },
    });

    const values = {
      ipd_enrollment_id: 0,
      price_per_item: 100,
      quantity: 2,
      ipd_bill_category_id: "cat1",
      ipd_bill_item_id: "item1",
      amount: 200,
    };

    const resetForm = jest.fn();
    const formikHelpers = { resetForm };

    await handleFormSubmit(values, formikHelpers);

    expect(axios.post).toHaveBeenCalledWith(
      "/api/doctor/ipd_enrollement_bill_items/create",
      { ...values, ipd_enrollment_id: 123 },
      { Authorization: "Bearer token" }
    );

    expect(toast.error).toHaveBeenCalledWith(
      "Failed to create item",
      expect.any(Object)
    );

    expect(resetForm).not.toHaveBeenCalled();
  });

  it("should handle API error", async () => {
    axios.post.mockRejectedValue(new Error("Network Error"));

    const values = {
      ipd_enrollment_id: 0,
      price_per_item: 100,
      quantity: 2,
      ipd_bill_category_id: "cat1",
      ipd_bill_item_id: "item1",
      amount: 200,
    };

    const resetForm = jest.fn();
    const formikHelpers = { resetForm };

    await handleFormSubmit(values, formikHelpers);

    expect(axios.post).toHaveBeenCalledWith(
      "/api/doctor/ipd_enrollement_bill_items/create",
      { ...values, ipd_enrollment_id: 123 },
      { Authorization: "Bearer token" }
    );

    expect(resetForm).not.toHaveBeenCalled();
  });
});
