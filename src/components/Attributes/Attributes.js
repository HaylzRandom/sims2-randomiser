import { useEffect, useState } from 'react';

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

const Attributes = ({ gender }) => {
	const [turnOns, setTurnOns] = useState([]);
	const [turnOff, setTurnOff] = useState('');

	useEffect(() => {}, [gender]);

	const generateTurnOnsOffs = () => {
		let count = 1;
		let values = [];

		while (count <= 3) {
			let arrVal;

			if (count !== 3) {
				arrVal =
					turnOnsOffArr[Math.floor(Math.random() * turnOnsOffArr.length)];

				values.push(turnOnsOffArr.filter((val) => val === arrVal));
				console.log('Values', values);

				console.log(arrVal, count);
				console.log('TurnOns', turnOns);
			} else {
				setTurnOff(
					turnOnsOffArr[Math.floor(Math.random() * turnOnsOffArr.length)]
				);
			}

			count++;
		}
		console.log('Values end', values);
		setTurnOns(values, ...turnOns);
		console.log(turnOff);
		console.log(turnOns);
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
								<span className='title'>Aspiration: </span>
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Zodiac Sign: </span>
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
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Personality Rolls: </span>
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Hobby Rolls: </span>
							</p>
						</li>
						<li>
							<p>
								<span className='title'>Favourite Colour: </span>
							</p>
						</li>
					</ul>
				</div>
			</section>
		</>
	);
};
export default Attributes;
