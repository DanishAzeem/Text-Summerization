from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# text = """This is a Wolf #scary Welcome to the #Jungle, the number to know, Remember to the - John I      Love        You, John's show"""
# text = """ Thank you all so very much. Thank you to the Academy. !
#                Thank you to all of you in this room? I have to congratulate
#                the other incredible nominees this year. The Revenant was
#                the product of the tireless efforts of an unbelievable cast
#                and crew. First off, to my brother in this endeavor, Mr. Tom
#                Hardy. Tom, your talent on screen can only be surpassed by
#                your friendship off screen … thank you for creating at
#                ranscendent cinematic experience. Thank you to everybody at
#                Fox and New Regency … my entire team. I have to thank
#                everyone from the very onset of my career … To my parents;
#                none of this would be possible without you. And to my
#                friends, I love you dearly; you know who you are. And lastly,
#                I just want to say this: Making The Revenant was about
#                man's relationship to the natural world. A world that we
#                collectively felt in 2015 as the hottest year in recorded
#                history. Our production needed to move to the southern
#                tip of this planet just to be able to find snow. Climate
#                change is real, it is happening right now. It is the most
#                urgent threat facing our entire species, and we need to work
#                collectively together and stop procrastinating. We need to
#                support leaders around the world who do not speak for the
#                big polluters, but who speak for all of humanity, for the
#                indigenous people of the world, for the billions and
#                billions of underprivileged people out there who would be
#                most affected by this. For our children’s children, and
#                for those people out there whose voices have been drowned
#                out by the politics of greed. I thank you all for this
#                amazing award tonight. Let us not take this planet for
#                granted. I do not take tonight for granted. Thank you so very much.  """


def summarizer(text, Sum_ratio):

    stop_words = set(stopwords.words('english'))
    # print(stop_words)

    tokenize_words = word_tokenize(text.lower())
    # print(tokenize_words)

    word_freq = {}
    for word in tokenize_words:
        if word not in stop_words and word not in punctuation:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    # print(word_freq.keys())

    common_keywords = []
    counter = 0
    for word in word_freq.keys():
        common_keywords.append(word)
        counter += 1

    # print("Total common_keywordsn\n", common_keywords)
    # print("Counter = ", counter)

    ratio_float = float(Sum_ratio)
    ratio_int = int(counter * ratio_float)

    # print("\n\nSum_ratio = ", Sum_ratio)
    # print("\n\n")

    # i = 0
    # while i == 0 or i < ratio_int:
    #     common_keywords[i]
    #     print(common_keywords[i])
    #     i += 1

    keywords = []
    j = 0
    while j == 0 or j < ratio_int:
        keywords.append(common_keywords[j])
        # print(keywords[j])
        j += 1

    return keywords
    # return keywords, Sum_ratio
