import { useEffect, useState } from 'react';

import './attributes.css';

const aspirationsArr = [
	'Family',
	'Fortune',
	'Pleasure',
	'Knowledge',
	'Romance',
	'Popularity',
];

const zodiacsArr = [
	'Aries',
	'Taurus',
	'Gemini',
	'Cancer',
	'Leo',
	'Virgo',
	'Libra',
	'Scorpio',
	'Sagittarius',
	'Capricorn',
	'Aquarius',
	'Pisces',
];

const turnOnsOffArr = [
	'Cologne',
	'Poor',
	'Fatness',
	'Fitness',
	'Formal Wear',
	'Underwear and Swimwear',
	'Rich',
	'Supernatural',
	'Facial Hair',
	'Glasses',
	'Makeup',
	'Educated',
	'Good Reputation',
	'Bad Reputation',
	'Blonde Hair',
	'Red Hair',
	'Brown Hair',
	'Black Hair',
	'Talented',
	'Grey Hair',
	'Hard Worker',
	'Unemployed',
	'Logical',
	'Charismatic',
	'Great Cook',
	'Mechanical',
	'Creative',
	'Athletic',
	'Good at Cleaning',
	'Great Dancer',
	'Sci-Fi',
	'Brown Eyes',
	'Green Eyes',
	'Blue Eyes',
];

const Attributes = ({ generateSim }) => {
	const [turnOns, setTurnOns] = useState([]);
	const [turnOff, setTurnOff] = useState('');
	const [favouriteColour, setFavouriteColour] = useState('#2563de');

	useEffect(() => {
		generateFavouriteColour();
		generateTurnOnsOffs();
	}, [generateSim]);

	const generateZodiacSign = () => {
		return zodiacsArr[Math.floor(Math.random() * zodiacsArr.length)];
	};

	const generateAspiration = () => {
		return aspirationsArr[Math.floor(Math.random() * aspirationsArr.length)];
	};

	const generateFavouriteColour = () => {
		setFavouriteColour('#' + Math.floor(Math.random() * 16777215).toString(16));
	};

	// Need to find a better method
	const generateTurnOnsOffs = () => {
		let count = 1;
		let values = [];
		let newTurnOns = [];

		while (count <= 3) {
			values.push(
				turnOnsOffArr[Math.floor(Math.random() * turnOnsOffArr.length)]
			);

			count++;
		}

		newTurnOns.push(values[0]);
		newTurnOns.push(values[1]);
		setTurnOff(values[2]);

		setTurnOns(newTurnOns);
	};

	const generateRandomRoll = () => {
		return Math.floor(Math.random() * (10 - 1 + 1)) + 1;
	};

	return (
		<>
			<section id='sim__attributes'>
				<header>
					<h2>Attributes</h2>
				</header>
				<div className='sim-attributes'>
					<ul className='sim-attributes__list'>
						<li>
							<p>
								<span className='title'>Aspiration: </span>{' '}
								{generateAspiration()}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Zodiac Sign: </span>{' '}
								{generateZodiacSign()}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Turn Ons: </span>
								{turnOns[0]} | {turnOns[1]}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Turn Offs: </span> {turnOff}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Interest Rolls: </span>
								{generateRandomRoll()}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Personality Rolls: </span>
								{generateRandomRoll()}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Hobby Rolls: </span>
								{generateRandomRoll()}
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Favourite Colour: </span>{' '}
								<span
									className='colour'
									style={{ backgroundColor: favouriteColour }}>
									{favouriteColour}
								</span>
							</p>
						</li>
					</ul>
				</div>
			</section>
		</>
	);
};
export default Attributes;
