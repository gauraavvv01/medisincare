def recommendations(disease):

    if disease == "Dimorphic hemmorhoids(piles)":
        return {
            "title": "Dimorphic Hemorrhoids (Piles)",
            "remedies": [
                "Aloe Vera: Soothes burning and reduces swelling.",
                "Coconut Oil: Moisturizes and reduces inflammation.",
                "Ice Packs: Applying ice or cold packs to the hemorrhoid may help relieve pain and inflammation.",
                "Warm Baths: A soak in water with a temperature slightly higher than the average human body temperature."
            ],
            "diet_plan": [
                "Breakfast: 1 Cup of oats or upma with 1 cup milk.",
                "Lunch: Half cup rice, roti, kidney beans curry, snake gourd curry, buttermilk.",
                "Snacks: Three oatmeal or digestive biscuits with milk.",
                "Dinner: Roti with half cup ridge gourd curry."
            ],
            "exercises": [
                "Baddha Konasana (Bound Angle Pose): Stretches the groin, adductors (inner thighs), knees, strengthens the pelvic floor, psoas muscles, and hip flexors.",
                "Balasana (Child Pose): A restorative yogic asana known for its grounding, calming, and relaxing effects.",
                "Pawanmuktasana (Wind Relieving Pose): A yoga pose that helps with digestion, gas release, and abdominal relaxation.",
                "Pelvic Floor Exercises: A group of exercises aimed at strengthening your pelvic floor muscles."
            ]
        }
    
    elif disease == "Diabetes":
        return {
            "title": "Diabetes",
            "remedies": [
                "Bitter Gourd (Karela): Lowers blood sugar levels; consume cooked or as juice on an empty stomach.",
                "Indian Gooseberry (Amla): Rich in vitamin C; eat raw or mix juice with bitter gourd.",
                "Mango Leaves: Dry and grind tender leaves; consume as powder with water twice daily.",
                "Fenugreek: Enhances glucose tolerance; consume powdered seeds with water or milk.",
                "Cinnamon: Enhances insulin sensitivity; soak in water and drink on an empty stomach.",
                "Aloe Vera: Lowers blood sugar; drink two tablespoons of juice daily."
            ],
            "diet_plan": [
                "Whole Grains: Opt for brown rice, oats, whole wheat, and millet to manage blood sugar.",
                "Nuts and Seeds: Include walnuts, almonds, flax seeds, pumpkin seeds for stable blood sugar.",
                "Green Leafy Vegetables: Include spinach, drumstick leaves, and amaranth.",
                "Milk and Dairy: Choose low-fat options to control fat intake.",
                "Tender Coconut Water: Low GI and nutrient-rich, safe for controlled diabetics."
            ],
            "exercises": [
                "Surya Namaskar: Improves blood circulation and reduces stress.",
                "Trikonasana: Increases flexibility, strengthens the spine, and reduces insulin resistance.",
                "Tadasana: Improves posture and strengthens legs."
            ]
        }

    elif disease == "Bronchial Asthma":
        return {
            "title": "Bronchial Asthma",
            "remedies": [
                "Turmeric (Curcumin): Anti-inflammatory properties aid in easing breathing difficulties.",
                "Garlic: Reduces airway inflammation and respiratory issues.",
                "Black Seed: Contains thymoquinone, which reduces allergic reactions.",
                "Honey: Soothes the throat and acts as an expectorant, helping to loosen mucus."
            ],
            "diet_plan": [
                "Fresh Fruits and Vegetables: A variety to reduce inflammation and support lung health.",
                "Anti-inflammatory Nutrients: Foods rich in vitamins C, E, and A, like bell peppers and almonds.",
                "Avoid Trigger Foods: Processed foods and sulfite-rich foods like wine and dried fruits."
            ],
            "exercises": [
                "Pursed Lip Breathing: Enhances oxygen intake and eases breathlessness.",
                "Diaphragmatic Breathing: Deep abdominal breathing strengthens lung function.",
                "Cobra Pose: Opens the chest and improves lung capacity."
            ]
        }

    elif disease == "Cervical spondylosis":
        return {
            "title": "Cervical Spondylosis",
            "remedies": [
                "Exercise: Walking and swimming reduce stiffness in neck and shoulders.",
                "Hot and Cold Compresses: Alternating to relax muscles and reduce inflammation.",
                "Garlic, Turmeric, and Ginger: Alleviate pain due to their anti-inflammatory properties.",
                "Sesame Seeds: Rich in essential nutrients to support bone health."
            ],
            "diet_plan": [
                "Calcium-Rich Diet: Include milk, cottage cheese, almonds, and sesame seeds.",
                "Fiber and Vitamin C: Incorporate whole grains and fresh vegetables for joint health.",
                "Avoid: Red meat, white potatoes, coffee, and oily foods."
            ],
            "exercises": [
                "Setu Bandhasana (Bridge Pose): Strengthens neck muscles.",
                "Bhujangasana (Cobra Pose): Stretches the neck, shoulders, and upper back.",
                "Tadasana (Mountain Pose): Improves posture and reduces neck strain."
            ]
        }


    elif disease == "Paralysis (brain hemorrhage)":
        return {
            "title": "Paralysis (Brain Hemorrhage)",
            "remedies": [
                "Acupuncture: Increases blood flow and BDNF production, aiding recovery.",
                "Brain-Healthy Foods: Salmon, blueberries, and avocados reduce inflammation.",
                "Herbal Teas: Ginger, chamomile, and peppermint alleviate nausea and inflammation."
            ],
            "diet_plan": [
                "Omega-3 Fatty Acids: Include salmon, flaxseeds, and walnuts.",
                "Brain-supporting Foods: Avocados, eggs, and green tea for cognitive support.",
                "Hydration: Maintain fluid intake to support cellular repair."
            ],
            "exercises": [
                "Range of Motion Exercises: For flexibility and mobility.",
                "Balance Training: Exercises like single-leg stance for coordination.",
                "Strength Training: Squats, lunges, or resistance bands to restore muscle function.",
                "Cognitive Training: Puzzles and reading exercises to improve cognitive function."
            ]
        }


    elif disease == "Urinary tract infection":
        return {
            "title": "Urinary Tract Infection",
            "remedies": [
                "Hydration: Drink plenty of water to flush bacteria out of the system.",
                "Probiotics: Yogurt and other probiotics maintain a healthy gut.",
                "Garlic: Antimicrobial properties help prevent bacterial growth.",
                "D-Mannose: Found in cranberries, prevents harmful bacteria from sticking to the urinary tract."
            ],
            "diet_plan": [
                "Early Morning: Lukewarm water, garlic water, or herbal tea.",
                "Breakfast: Include whole grains like semolina or oats.",
                "Cranberry Juice: Known for preventing bacteria from attaching to the urinary tract."
            ],
            "exercises": [
                "Tadasana (Mountain Pose): Improves posture, enhancing the bladder's position.",
                "Bridge Pose (Setu Bandhasana): Strengthens pelvic muscles for bladder support.",
                "Child's Pose (Balasana): Reduces bladder tension through gentle pelvic stretches."
            ]
        }


    elif disease == "Arthritis":
        return {
            "title": "Arthritis",
            "remedies": [
                "Heat and Cold: Heat loosens joints, cold reduces inflammation.",
                "Turmeric: Anti-inflammatory properties help reduce joint pain.",
                "Fish Oil: Reduces symptoms of rheumatoid arthritis."
            ],
            "diet_plan": [
                "Omega-3 Rich Foods: Salmon, chia seeds, and walnuts to reduce inflammation.",
                "Anti-inflammatory Foods: Leafy greens, bell peppers, and berries.",
                "Avoid Processed Foods: These can increase inflammation."
            ],
            "exercises": [
                "Chair Pose: Strengthens legs and improves support for the knee joints.",
                "Tree Pose: Enhances balance, which can reduce stress on joints.",
                "Cat-Cow Pose: Increases flexibility in the spine."
            ]
        }


    elif disease == "Acne":
        return {
            "title": "Acne",
            "remedies": [
                "Zinc: An essential mineral for reducing inflammation.",
                "Honey and Aloe Vera: Natural anti-inflammatory properties."
            ],
            "diet_plan": [
                "Low Glycemic Foods: Whole grains, vegetables, and legumes to manage insulin levels.",
                "Reduce Dairy Intake: High dairy intake can increase acne."
            ],
            "exercises": [
                "Fish Pose (Matsyasana): Boosts blood circulation, enhancing skin health.",
                "Bhujangasana (Cobra Pose): Improves blood flow to the face and skin."
            ]
        }

    elif disease == "Hyporthyroidism":
        return {
            "title": "Hyperthyroidism",
            "remedies": [
                "Selenium: Brazil nuts and tuna support thyroid hormone metabolism.",
                "Sugar-free Diet: Reduces inflammation and supports thyroid function."
            ],
            "diet_plan": [
                "Iodine-Rich Foods: Fish, eggs, and iodized salt to support thyroid function."
            ],
            "exercises": [
                "Supported Shoulder Stand: Stimulates the thyroid gland.",
                "Boat Pose (Navasana): Strengthens core muscles and supports metabolism."
            ]
        }


    elif disease == "hepatitis A":
        return {
            "title": "Hepatitis A",
            "remedies": [
                "Balanced Diet: Leafy greens, sweet potatoes, and citrus fruits to support liver recovery.",
                "Ginger Tea: Anti-inflammatory properties to reduce liver inflammation.",
                "Coconut water aids hydration and detoxification.",
                "Boil cumin seeds and coriander seeds in water and drink as tea."
            ],
            "diet_plan": [
                "Hydration: Plenty of water and herbal teas to support detoxification.",
                "Breakfast: Oatmeal or semolina porridge with almond milk. Fresh fruit (banana, papaya, apple) and herbal tea.",
                "Lunch: Steamed rice with lentil soup (dal) and boiled vegetables.",
                "Snacks: A small salad with grated carrots, cucumber, and olive oil.",
                "Dinner: Whole wheat chapati with lightly spiced vegetable curry.",
                "A bowl of curd or plain yogurt (if digestion is fine)."
            ],
            "exercises": [
                "Kapalbhati Pranayama: Breathing technique for liver detox.",
                "Dhanurasana (Bow Pose): Improves blood flow and supports liver health.",
                "Naukasana (Boat Pose): Enhances digestion and reduces liver congestion."
            ]
        }

        
    elif disease == "Hepatitis B":
        return {
            "title": "Hepatitis B",
            "remedies": [
                "Drink dandelion root tea or milk thistle tea for liver regeneration.",
                "Add 1 tsp of apple cider vinegar to a glass of water and drink before meals.",
                "Balanced Diet: Leafy greens, sweet potatoes, and citrus fruits to support liver recovery.",
                "Ginger Tea: Anti-inflammatory properties to reduce liver inflammation.",
                "Coconut water aids hydration and detoxification.",
                "Boil cumin seeds and coriander seeds in water and drink as tea.",
                "Milk Thistle Tea: Known for liver-regeneration properties.",
                "Raw Garlic: Consume 1-2 cloves on an empty stomach to boost immunity and detoxify.",
                "Carrot-Beetroot Juice: Blend carrot, beetroot, and a pinch of ginger for liver cleansing."
            ],
            "diet_plan": [
                "Breakfast: Whole-grain bread with avocado, green tea, and a handful of walnuts.",
                "Lunch: Grilled chicken or tofu, quinoa, and a salad with olive oil dressing.",
                "Snacks: A cup of green tea with roasted sunflower seeds or flaxseeds.",
                "Dinner: Lentil soup, brown rice, and steamed broccoli."
            ],
            "exercises": [
                "Bhujangasana (Cobra Pose): Improves liver function and relieves stress.",
                "Dhanurasana (Bow Pose): Strengthens the abdominal organs and reduces liver congestion.",
                "Kapalabhati Pranayama: Detoxifies and oxygenates the liver."
            ]
        }

    elif disease == "Hepatitis C":
        return {
            "title": "Hepatitis C",
            "remedies": [
                "Dandelion Root Tea: Aids liver detoxification and regeneration. Drink 1-2 cups daily.",
                "Aloe Vera Juice: Consume 2 tbsp of fresh aloe vera juice before meals for liver health.",
                "Turmeric Milk: Mix 1/2 tsp turmeric in warm milk and drink before bed for anti-inflammatory effects."
            ],
            "diet_plan": [
                "Breakfast: Smoothie with spinach, berries, chia seeds, and almond milk.",
                "Lunch: Grilled salmon or mackerel, sweet potatoes, and steamed asparagus.",
                "Snacks: Green tea and a handful of almonds.",
                "Dinner: Vegetable stew, quinoa, and sautéed kale."
            ],
            "exercises": [
                "Naukasana (Boat Pose): Enhances liver function and strengthens the core.",
                "Matsyasana (Fish Pose): Improves circulation to the liver and relieves stress.",
                "Anulom Vilom (Alternate Nostril Breathing): Promotes relaxation and boosts immunity."
            ]
        }


    elif disease == "Hepatitis D":
        return {
            "title": "Hepatitis D",
            "remedies": [
                "Apple Cider Vinegar: Add 1 tsp of ACV to a glass of warm water and drink before meals.",
                "Garlic Infusion: Crush 2 cloves of garlic and soak in water overnight. Drink the water in the morning.",
                "Turmeric-Honey Paste: Mix 1 tsp turmeric with honey. Consume once daily to reduce inflammation."
            ],
            "diet_plan": [
                "Breakfast: Whole grain toast with almond butter, an orange, and green tea.",
                "Lunch: Steamed fish, brown rice, and sautéed spinach with garlic.",
                "Snacks: Fresh pomegranate juice or roasted pumpkin seeds.",
                "Dinner: Lentil soup, a small portion of grilled chicken, and steamed carrots."
            ],
            "exercises": [
                "Paschimottanasana (Seated Forward Bend): Stimulates liver function and relieves abdominal tension.",
                "Tadasana (Mountain Pose): Improves posture and circulation.",
                "Bhramari Pranayama (Bee Breathing): Relieves stress and boosts immunity."
            ]
        }


    elif disease == "Hepatitis E":
        return {
            "title": "Hepatitis E",
            "remedies": [
                "Coconut Water: Replenishes electrolytes and promotes hydration.",
                "Mint-Coriander Juice: Blend mint leaves, coriander leaves, and lemon juice. Drink twice daily.",
                "Ajwain Water: Boil 1 tsp of carom seeds in water and drink to improve digestion."
            ],
            "diet_plan": [
                "Breakfast: Semolina porridge with banana and a glass of buttermilk.",
                "Lunch: Rice, plain yogurt, and boiled vegetables (potatoes, beans, carrots).",
                "Snacks: Coconut water or a slice of watermelon.",
                "Dinner: Light vegetable soup with whole wheat bread."
            ],
            "exercises": [
                "Vajrasana (Thunderbolt Pose): Improves digestion and eases abdominal discomfort.",
                "Setu Bandhasana (Bridge Pose): Stimulates abdominal organs and reduces bloating.",
                "Deep Diaphragmatic Breathing: Supports liver health and relaxation."
            ]
        }

    elif disease == "Tuberculosis":
        return {
            "title": "Tuberculosis",
            "remedies": [
                "Garlic: Contains sulfuric acid which combats the TB bacteria.",
                "Amla: Boosts immunity and fights bacteria.",
                "Black Pepper: Reduces chest pain and coughing symptoms.",
                "Milk: Rich in calcium and vitamin D, both help treat tuberculosis and its severe symptoms.",
                "Green Tea: Antioxidant polyphenol in green tea combats tuberculosis bacteria.",
                "Mint: Has anti-bacterial properties and helps in the healing of tissues damaged by tuberculosis."
            ],
            "diet_plan": [
                "Breakfast: Cottage Cheese sandwich with 1 glass skimmed milk or two eggs with soaked walnuts.",
                "Lunch: 1 cup rice with 1 cup soya chunk curry, 2-3 roti, 1 cup moong dal.",
                "Snacks: 6 soaked almonds, 2 cashews, walnuts.",
                "Dinner: 2 paneer stuffed capsicum, roti, mix veg curry."
            ],
            "exercises": [
                "Bhujangasana (Cobra Pose): Opens the chest to improve lung capacity.",
                "Bhastrika (Breath of Fire): Clears respiratory tract.",
                "Kapalbhati Pranayam (Breath of Fire): Elevates lung capacity and supports liver and kidney performance.",
                "Tadasana (Tree Pose): Strengthens bronchioles and lungs, improving respiratory system regulation.",
                "Trikonasana (Triangle Pose): Restores immune system and liver functionality."
            ]
        }

    elif disease == "Pneumonia":
        return {
            "title": "Pneumonia",
            "remedies": [
                "Gargling Saltwater: Helps break up mucus.",
                "Honey: Provides antibacterial benefits and eases throat discomfort.",
                "Citrus fruits: Known for their vitamin C content, which has antioxidant properties and magnifies the antibacterial properties of other substances to help combat pneumonia.",
                "Ginger or Turmeric Tea: Drinking warm tea made with turmeric root or fresh ginger may help decrease pain."
            ],
            "diet_plan": [
                "Breakfast: Milk and cornflakes.",
                "Lunch: Parboiled rice, yellow curry, chicken.",
                "Snacks: Carrot soup or vegetable soup.",
                "Dinner: Boiled rice with mashed potatoes and salad. Milk after dinner for better digestion."
            ],
            "exercises": [
                "Vajrasana (Thunderbolt Pose): Improves digestion, bowel movements, and relieves constipation.",
                "Paschimottanasana: Helps relieve lower back pain and stiffness, improves flexibility, and reduces anxiety.",
                "Ushtrasana (Camel Pose): A back-bending yoga posture that potentially activates brain cells for optimal functioning.",
                "Balasana (Child Pose): A restorative yogic asana known for its grounding, calming, and relaxing effects."
            ]
        }


    elif disease == "Malaria":
        return {
            "title": "Malaria",
            "remedies": [
                "Ginger Tea: Helps reduce nausea and body aches. Boil ginger in water and drink 1-2 cups daily.",
                "Lime Water: Helps manage fever with its acidic content."
            ],
            "diet_plan": [
                "High protein intake.",
                "Fresh fruit juices."
            ],
            "exercises": [
                "Balasana (Child’s Pose): Promotes relaxation.",
                "Shavasana (Corpse Pose): Aids in deep relaxation."
            ]
        }


    elif disease == "Chicken pox":
        return {
            "title": "Chicken Pox",
            "remedies": [
                "Oatmeal bath: Soothes itching and irritation.",
                "Neem leaves: Applying paste helps relieve itching."
            ],
            "diet_plan": [
                "Soft foods (soups, mashed potatoes, yogurt) to avoid mouth irritation."
            ],
            "exercises": [
                "Shavasana (Corpse Pose): For relaxation.",
                "Cat-Cow Stretches (Marjaryasana/Bitilasana): For mild movement."
            ]
        }

    elif disease == "Dengue":
        return {
            "title": "Dengue",
            "remedies": [
                "Papaya leaf extract: Helps increase platelet count.",
                "Neem leaf decoction: Helps boost immunity."
            ],
            "diet_plan": [
                "Papaya leaves: Crucial for boosting platelets."
            ],
            "exercises": [
                "Complete bed rest during dengue fever.",
                "Viparita Karani: For improving blood circulation."
            ]
        }
  

    elif disease == "Typhoid":
        return {
            "title": "Typhoid",
            "remedies": [
                "Apple cider vinegar: Helps reduce fever.",
                "Garlic: Strengthens immunity and fights bacteria."
            ],
            "diet_plan": [
                "Soft, easily digestible foods (porridge, khichdi)."
            ],
            "exercises": [
                "Anulom Vilom for calming.",
                "No strenuous activities until complete recovery."
            ]
        }

    elif disease == "Hyperthyroidism":
        return {
            "title": "Hyperthyroidism",
            "remedies": [
                "Lemon Balm Tea: Brew lemon balm tea to calm overactive thyroid symptoms. Drink 1-2 cups daily.",
                "Bugleweed (Lycopus): Take bugleweed extract (consult a healthcare provider for dosage).",
                "Ashwagandha: Take ashwagandha supplements or tea to support thyroid health.",
                "Seaweed: Avoid iodine-rich seaweed to manage thyroid activity."
            ],
            "diet_plan": [
                "Avoid caffeine and iodine-rich foods (e.g., iodized salt, shellfish).",
                "Include cruciferous vegetables (broccoli, cauliflower).",
                "Eat protein-rich foods (beans, lentils).",
                "Snack on antioxidant-rich fruits like berries and cherries."
            ],
            "exercises": [
                "Shoulder Stand (Sarvangasana): Balances thyroid function.",
                "Fish Pose (Matsyasana): Stimulates the thyroid gland.",
                "Ujjayi Pranayama: A calming breathing technique.",
                "Cat-Cow Stretch: Improves blood flow to the thyroid region."
            ]
        }


    elif disease == "Osteoarthristis":
        return {
            "title": "Osteoarthritis",
            "remedies": [
                "Turmeric and Ginger Tea: Anti-inflammatory properties help reduce pain and stiffness.",
                "Epsom Salt Soak: Add 2 cups to warm bathwater for joint pain relief.",
                "Cold and Heat Packs: Alternate for 15-20 minutes to soothe inflammation.",
                "Apple Cider Vinegar: Mix 1 tbsp in warm water; drink twice daily for detox."
            ],
            "diet_plan": [
                "Add omega-3 fatty acids (salmon, walnuts) to reduce inflammation.",
                "Include calcium and vitamin D-rich foods (milk, spinach).",
                "Focus on whole grains and fiber (oats, brown rice).",
                "Avoid processed and sugary foods."
            ],
            "exercises": [
                "Chair Yoga: Gentle poses to reduce stiffness.",
                "Swimming: Low-impact activity to improve joint mobility.",
                "Quadriceps Strengthening: Straight leg raises to support knee joints.",
                "Tai Chi: Improves balance and reduces joint stress."
            ]
        }

    elif disease == "Fungal infection":
        return {
            "title": "Fungal Infection",
            "remedies": [
                "Tea Tree Oil: Apply diluted tea tree oil (3 drops in a carrier oil) to the affected area twice daily.",
                "Garlic: Crush garlic and apply it topically or consume it raw for antifungal effects.",
                "Coconut Oil: Use virgin coconut oil directly on the skin as an antifungal agent.",
                "Aloe Vera Gel: Apply fresh aloe vera gel to soothe and heal infected areas."
            ],
            "diet_plan": [
                "Avoid refined carbs and sugar to starve fungi.",
                "Include fermented foods (yogurt, kimchi) for probiotics.",
                "Drink green tea for its antifungal properties.",
                "Eat garlic and onion regularly for their natural antifungal effects."
            ],
            "exercises": [
                "Sun Salutation (Surya Namaskar): Boosts immunity and circulation.",
                "Kapalabhati Pranayama: Detoxifies and supports skin health.",
                "Seated Forward Bend (Paschimottanasana): Enhances gut health and immunity.",
                "Twisting Poses: Aid detoxification and reduce fungal overgrowth."
            ]
        }


    elif disease == "Allergy":
        return {
            "title": "Allergy",
            "remedies": [
                "Local Honey: Consume 1 tsp of local honey daily to build immunity to local allergens.",
                "Neti Pot: Use saline water in a neti pot to clear nasal passages.",
                "Quercetin: Include quercetin-rich foods like onions, apples, and berries.",
                "Peppermint Tea: Helps open nasal passages and ease congestion."
            ],
            "diet_plan": [
                "Avoid common allergens (nuts, dairy, gluten if sensitive).",
                "Eat anti-inflammatory foods (turmeric, ginger, leafy greens).",
                "Snack on foods rich in omega-3s (flaxseeds, chia seeds).",
                "Drink plenty of water to stay hydrated and flush allergens."
            ],
            "exercises": [
                "Anulom Vilom: Cleanses nasal passages and calms the immune system.",
                "Bhujangasana (Cobra Pose): Expands the chest to improve breathing.",
                "Halasana (Plow Pose): Reduces congestion and improves blood flow.",
                "Child’s Pose (Balasana): Eases stress and respiratory discomfort."
            ]
        }

    
    elif disease == "Common Cold":
        return {
            "title": "Common Cold",
            "remedies": [
                "Hydration: Drink plenty of fluids to stay hydrated and ease congestion.",
                "Warm Liquids: Sip on warm drinks like tea or soup to soothe the throat and loosen mucus.",
                "Salt Water Gargle: Gargling with warm salt water reduces throat pain and swelling.",
                "Rest: Ensure adequate sleep and rest for quick recovery.",
                "Humidifier: Use a cool-mist humidifier to add moisture to the air.",
                "Garlic: Known for antimicrobial properties, helps in recovery."
            ],
            "diet_plan": [
                "Early Morning: Warm water",
                "Breakfast: Options like Veg Semolina, Broken Wheat Porridge, or Veg Vermicelli.",
                "Mid-Morning: Fruit, Fruit juice, or Herbal Tea",
                "Lunch: Chapatti with Vegetables or Dal with Salad",
                "Dinner: Include cereals like Barley and Millet."
            ],
            "exercises": [
                "Balasana (Child’s Pose): A calming pose that helps with chest and nasal congestion.",
                "Setu Bandhasana (Bridge Pose): Opens the chest and lungs to relieve symptoms.",
                "Dhanurasana (Bow Pose): Helpful for easing cold and cough symptoms."
            ]
        }

    elif disease == "Migraine":
        return {
            "title": "Migraine",
            "remedies": [
                "Lavender Oil: Helps relieve migraine pain and anxiety.",
                "Acupuncture: Known to alleviate headache symptoms.",
                "Peppermint Oil: Provides a cooling effect that can reduce headache pain.",
                "Hydration: Keep hydrated to avoid dehydration-related migraines.",
                "Stress Management: Practice relaxation techniques to reduce stress-induced migraines."
            ],
            "diet_plan": [
                "Whole Grains: Replace white bread, white rice, and pasta with whole grains.",
                "Fruits and Vegetables: Aim for half of your plate to be fruits and vegetables.",
                "Limit Sodium: Try to limit sodium intake for better blood pressure control.",
                "Foods Rich in Magnesium: Nuts can help soothe headache pain.",
                "Foods with Omega-3s: Fatty fish and seeds to help reduce inflammation."
            ],
            "exercises": [
                "Kneeling Pose: A calming pose to help ease migraine symptoms.",
                "Shavasana (Corpse Pose): Helps relax and relieve stress.",
                "Temple Circles: Gentle circular massages around the temples.",
                "Jaw Massage: Relieves tension in the jaw area which can help reduce migraines.",
                "Neck Rotation: Aids in relieving neck tension related to headaches."
            ]
        }

    elif disease == "Hypertension":
        return {
            "title": "Hypertension",
            "remedies": [
                "Exercise: Regular physical activity helps reduce blood pressure.",
                "DASH Diet: Focus on whole grains, fruits, and vegetables.",
                "Limit Salt: Reducing salt intake aids in managing blood pressure.",
                "Avoid Smoking and Limit Alcohol: Helps in blood pressure management.",
                "Relaxation Techniques: Practice deep breathing and meditation."
            ],
            "diet_plan": [
                "Fruits and Vegetables: Fresh options are rich in fiber and potassium.",
                "Whole Grains: Choose whole grains over refined grains.",
                "Low-fat Dairy: Can help lower systolic blood pressure.",
                "Lean Protein: Opt for skinless poultry and fish.",
                "Healthy Fats: Use olive or canola oil in cooking."
            ],
            "exercises": [
                "Bhadrasana (Butterfly Pose): A gentle pose to reduce stress.",
                "Viparita Karani (Legs Up): Improves blood circulation and reduces stress.",
                "Setu Bandhasana (Bridge Pose): Helps in blood pressure control.",
                "Balasana (Child's Pose): Reduces stress and tension in the body.",
                "Pranayama Breathing Techniques: Nadishodhana, Ujjayi, Sitali for relaxation."
            ]
        }

    elif disease == "Gastroenteritis":
        return {
            "title": "Gastroenteritis",
            "remedies": [
                "Hydration: Drink lots of fluids to replace what’s lost due to vomiting/diarrhea.",
                "Rest: Adequate rest is essential for a quicker recovery.",
                "Pain Relief: Take acetaminophen to ease fever and aches.",
                "Bland Foods: Start with easy-to-digest foods like toast, rice, bananas."
            ],
            "diet_plan": [
                "Fluids: Small sips of clear fluids like water or broth every few minutes.",
                "BRAT Diet: Bananas, Rice, Applesauce, and Toast for gentle digestion.",
                "Soft Foods: After improvement, try oatmeal, soft-cooked eggs, or steamed veggies."
            ],
            "exercises": [
                "Balasana (Child’s Pose): Gentle pose for gastric relief.",
                "Vajrasana: Can be done even after meals to aid digestion.",
                "Paschimottanasana (Seated Forward Bend): Helps alleviate gastric symptoms.",
                "Leg Raises: Helps with abdominal strengthening and digestion.",
                "Knee Hug: Relieves gas and eases abdominal discomfort."
            ]
        }

    elif disease == "GERD":
        return {
            "title": "Gastroesophageal Reflux Disease (GERD)",
            "remedies": [
                "Avoid trigger foods: Reduce intake of fatty, spicy foods, chocolate, caffeine, and alcohol.",
                "Smaller meals: Eat smaller meals to prevent overloading the stomach.",
                "Elevate head while sleeping: Helps prevent acid reflux at night.",
                "Avoid lying down immediately after meals: Wait 2-3 hours to avoid reflux."
            ],
            "diet_plan": [
                "High-fiber foods: Include oatmeal, whole grains, and root vegetables.",
                "Alkaline foods: Consume bananas, melons, and green vegetables to balance stomach acidity.",
                "Lean protein: Choose skinless poultry, fish, and legumes.",
                "Non-citrus fruits: Try apples, pears, and other low-acid fruits."
            ],
            "exercises": [
                "Gentle Yoga: Focus on poses that do not compress the stomach, like seated forward bend.",
                "Light Walking: Helps digestion, especially after meals.",
                "Deep breathing exercises: Can aid in relaxation and reduce stress-related GERD symptoms."
            ]
        }

    elif disease == "Chronic cholestasis":
        return {
            "title": "Chronic Cholestasis",
            "remedies": [
                "Avoid alcohol: Helps reduce liver strain.",
                "Manage itching: Use cool baths or oatmeal baths to soothe skin itching.",
                "Stay hydrated: Hydration is key for liver health and relieving symptoms.",
                "Low-fat diet: Reduces the burden on bile production and absorption."
            ],
            "diet_plan": [
                "High-fiber foods: Include oats, barley, and fruits for digestive support.",
                "Lean proteins: Opt for sources like chicken, fish, and legumes.",
                "Avoid fatty foods: Reduces liver workload and aids in better digestion.",
                "Vitamin-rich foods: Consume vegetables high in vitamins A, D, E, and K."
            ],
            "exercises": [
                "Gentle Yoga: Poses like Cat-Cow and Child’s Pose aid in liver function.",
                "Breathing Exercises: Help reduce stress and improve oxygenation.",
                "Low-impact cardio: Walking or light cycling improves overall health without overtaxing the liver."
            ]
        }

    elif disease == "Drug Reaction":
        return {
            "title": "Drug Reaction",
            "remedies": [
                "Stop the drug causing reaction (if identified and safe to do so).",
                "Hydrate: Drink water to help flush out toxins from the body.",
                "Use soothing balms: For skin reactions, apply gentle, hypoallergenic moisturizers.",
                "Avoid irritants: Avoid additional allergens or irritants to minimize symptoms."
            ],
            "diet_plan": [
                "Antioxidant-rich foods: Include berries, nuts, and leafy greens to support detoxification.",
                "Hydrating foods: Cucumbers, watermelon, and citrus fruits are helpful.",
                "Protein sources: Lean proteins to maintain strength and health.",
                "Avoid processed foods: Minimizes exposure to additional allergens or toxins."
            ],
            "exercises": [
                "Gentle Stretching: Avoid strenuous exercise if experiencing severe reactions.",
                "Deep Breathing: Helps reduce stress and supports recovery.",
                "Light walking: Can promote circulation and relaxation."
            ]
        }

    elif disease == "Peptic ulcer diseae":
        return {
            "title": "Peptic Ulcer Disease",
            "remedies": [
                "Probiotics: Include yogurt or kefir for gut health.",
                "Avoid spicy and acidic foods: Reduces stomach irritation.",
                "Ginger: Known to ease nausea and soothe the stomach lining.",
                "Small, frequent meals: Helps prevent overloading the stomach."
            ],
            "diet_plan": [
                "High-fiber foods: Oatmeal, apples, and carrots aid digestion.",
                "Lean proteins: Skinless poultry, tofu, and fish reduce stomach acid production.",
                "Non-acidic vegetables: Include leafy greens, sweet potatoes, and squash.",
                "Probiotic foods: Yogurt, miso, and sauerkraut support digestive health."
            ],
            "exercises": [
                "Child's Pose: A gentle yoga pose that can help relieve stomach pressure.",
                "Breathing Exercises: Focuses on relaxation to ease digestive stress.",
                "Light Walking: Aids in digestion without putting pressure on the stomach."
            ]
        }

    elif disease == "Impetigo":
        return {
            "title": "Impetigo",
            "remedies": [
                "Wash the sores with an antibacterial or antiseptic soap every 8 to 12 hours. Soak off any visible crust and pat dry with a clean towel each time.",
                "Cover the sores with a waterproof occlusive dressing to stop the infection from spreading. You can use a crepe bandage to hold the dressing in place.",
                "Apply fresh aloe vera gel or an ointment containing aloe vera to soothe irritated skin and promote healing.",
                "Apply honey or manuka honey to the affected area to inhibit bacterial growth and promote wound healing."
            ],
            "diet_plan": [
                "A balanced diet rich in fruits, vegetables.",
                "Lean proteins: Skinless poultry, tofu, and fish reduce stomach acid production.",
                "Foods high in vitamin C.",
                "Probiotic foods: Yogurt, miso, and sauerkraut support digestive health."
            ],
            "exercises": [
                "Go for a walk.",
                "Keeping your nails short: Keep your nails clean and short to avoid scratching the sores."
            ]
        }

    elif disease == "Varicose veins":
        return {
            "title": "Varicose Veins",
            "remedies": [
                "Get regular exercise. Walking is a great way to help blood flow in the leg.",
                "Manage weight. Losing excess pounds takes pressure off the veins.",
                "Avoid salt.",
                "Don't wear tight clothes."
            ],
            "diet_plan": [
                "Vitamin E: This vitamin is found in foods like avocados, sunflower seeds, and hazelnuts.",
                "Vitamin D: This vitamin helps your veins relax and contract, and helps keep the muscles that support them strong. Eggs, fish, and soy are good sources of vitamin D.",
                "High-fiber foods: Oatmeal, apples, and carrots aid digestion."
            ],
            "exercises": [
                "Swimming.",
                "Walking.",
                "Cycling."
            ]
        }

    elif disease == "Hypoglycemia":
        return {
            "title": "Hypoglycemia",
            "remedies": [
                "Eat or drink 15 to 20 grams of fast-acting carbohydrates. These are sugary foods or drinks without protein or fat that are easily converted to sugar in the body. Try glucose tablets or gel, fruit juice, regular (not diet) soda, honey, or sugary candy.",
                "Recheck blood sugar levels 15 minutes after treatment. If blood sugar levels are still under 70 mg/dL (3.9 mmol/L), eat or drink another 15 to 20 grams of fast-acting carbohydrate, and recheck your blood sugar level again in 15 minutes. Repeat these steps until the blood sugar is above 70 mg/dL (3.9 mmol/L).",
                "Have a snack or meal. Once your blood sugar is back in the standard range, eating a healthy snack or meal can help prevent another drop in blood sugar and replenish your body's glycogen stores."
            ],
            "diet_plan": [
                "Breakfast: Greek yogurt, fruit and granola OR Egg and cheese sandwich, and fruit.",
                "Snack: Fruit and cottage cheese OR Cheese and crackers.",
                "Lunch: Poke bowl (protein, rice/noodles, and veggies) OR Sandwich (protein, veggies and mayo/avocado) and fruit."
            ],
            "exercises": [
                "Anaerobic exercise: High-intensity interval training, short sprints, and resistance exercise can help prevent hypoglycemia and reduce the need for extra carbohydrates.",
                "Morning exercise: Exercising in the morning can be beneficial because insulin sensitivity is usually lower at that time.",
                "Brisk walking: A 30-minute walk after a meal can lower blood sugar levels."
            ]
        }

    elif disease == "Heart attack":
        return {
            "title": "Heart Attack",
            "remedies": [
                "Avoid smoking: If applicable, a person should stop smoking.",
                "Garlic is claimed to be a remedy for chest pain.",
                "Exercise or workout is physical activity that enhances or maintains fitness and overall health.",
                "Excess weight can lead to illnesses like high blood pressure, high cholesterol, and type 2 diabetes, all of which raise your risk of getting heart disease."
            ],
            "diet_plan": [
                "Fish high in omega-3 fatty acids (salmon, tuna, and trout).",
                "Lean meats such as lean ground beef or pork tenderloin or skinless chicken or turkey.",
                "Nuts, seeds, and soy products (tofu).",
                "Legumes such as kidney beans, lentils, chickpeas, black-eyed peas, and lima beans."
            ],
            "exercises": [
                "Apana Vayu Mudra: Also known as the Mrita Sanjeevani Mudra, this mudra is said to provide immediate relief to someone suffering from cardiac arrest.",
                "Shoulder stand pose (Sarvangasana): This pose can help burn fat, reduce blood pressure, and prevent heart problems.",
                "Big toe pose (Padangusthasana): This pose can strengthen your calves and thighs, relieve tension, and lower blood pressure."
            ]
        }

    else:
        return {
            "remedies": ["No specific remedies available."],
            "diet_plan": ["Follow a balanced diet."],
            "exercises": ["Consult a healthcare provider."]
        }
        


        


        



