import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# Realistic Browser Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

# Extensive list of major mobile brands in India
brands = [
    "samsung", 
    "apple", 
    "vivo", 
    "oppo", 
    "realme", 
    "xiaomi", 
    "oneplus", 
    "motorola", 
    "poco", 
    "iqoo", 
    "infinix", 
    "google pixel", 
    "nothing"
]

scraped_data = []

print(f"Starting Multi-Brand Mobile Scraping across {len(brands)} brands...\n")

for brand in brands:
    # URL encoded brand search
    query_brand = brand.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={query_brand}+mobiles"
    print(f"--> Scraping {brand.title()} devices...")
    
    try:
        response = requests.get(url, headers=headers, timeout=12)
        if response.status_code != 200:
            print(f"    Failed to fetch {brand} (Status: {response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Product cards container
        product_cards = soup.select("div[data-id]")
        
        count_for_brand = 0
        for card in product_cards:
            # Har brand ke top 12-15 phones capture karein
            if count_for_brand >= 15:
                break
                
            # 1. Product Title
            title = None
            img = card.select_one("img[alt]")
            if img and len(img["alt"]) > 5:
                title = img["alt"].strip()
            
            # 2. Pure Numeric Price Extraction (₹ symbol clean)
            price_val = None
            price_matches = card.find_all(string=re.compile(r"₹\s*[\d,]+"))
            if price_matches:
                raw_price = re.sub(r"[^\d]", "", price_matches[0])
                if raw_price:
                    price_val = int(raw_price)
            
            # 3. Dedicated Hardware Specifications Parsing
            ram = "N/A"
            storage = "N/A"
            resolution = "N/A"
            
            spec_list = card.select("ul li")
            for li in spec_list:
                text = li.get_text()
                
                # Extract RAM & Storage
                if "RAM" in text and "ROM" in text:
                    ram_match = re.search(r"(\d+\s*GB)\s*RAM", text, re.IGNORECASE)
                    rom_match = re.search(r"(\d+\s*(?:GB|TB))\s*ROM", text, re.IGNORECASE)
                    if ram_match: ram = ram_match.group(1)
                    if rom_match: storage = rom_match.group(1)
                elif "ROM" in text and storage == "N/A":
                    # Apple devices often only state ROM (e.g., 128 GB ROM)
                    rom_match = re.search(r"(\d+\s*(?:GB|TB))\s*ROM", text, re.IGNORECASE)
                    if rom_match: storage = rom_match.group(1)
                elif "RAM" in text and ram == "N/A":
                    ram_match = re.search(r"(\d+\s*GB)", text)
                    if ram_match: ram = ram_match.group(1)

                # Screen Display & Resolution
                if any(k in text for k in ["Display", "Resolution", "cm (", "inch", "FHD+", "AMOLED"]):
                    if resolution == "N/A":
                        resolution = text.strip()

            # Record valid mobile entry
            if title and price_val:
                scraped_data.append({
                    "Brand": brand.title(),
                    "Model_Name": title,
                    "Price_INR": price_val,
                    "RAM": ram,
                    "Storage": storage,
                    "Screen_Display": resolution
                })
                count_for_brand += 1
        
        print(f"    Fetched {count_for_brand} models for {brand.title()}.")
        time.sleep(1.2)  # Server safe delay
        
    except Exception as e:
        print(f"    Error scraping {brand}: {e}")

# Create DataFrame
df = pd.DataFrame(scraped_data)

if not df.empty:
    # Remove any duplicate rows
    df.drop_duplicates(subset=["Model_Name"], inplace=True)
    
    output_filename = "smartphones_clean.csv"
    # utf-8-sig keeps numeric values and Hindi/special symbols intact in Excel
    df.to_csv(output_filename, index=False, encoding="utf-8-sig")
    
    print("\n" + "="*50)
    print("--- Web Scraping Completed Successfully! ---")
    print(f"Total Unique Smartphones Scraped: {len(df)}")
    print(f"Brands Covered: {', '.join(df['Brand'].unique())}")
    print(f"Dataset Saved as: {output_filename}")
    print("="*50 + "\n")
    print(df[["Brand", "Model_Name", "Price_INR", "RAM", "Storage"]].head(12))
else:
    print("No data collected. Check internet connection.")